import pandas
import os
import transformers

from ..random_tools import get_os_random_seed, set_all_random_seeds


def default_model_and_tokenizer(model_name):
    model = transformers.BertForMultipleChoice.from_pretrained(model_name)
    tokenizer = transformers.BertTokenizer.from_pretrained(model_name)
    return model, tokenizer


class BertMultipleChoiceWrapper:
    def __init__(self, model, tokenizer, choices):
        self._model = model
        self._tokenizer = tokenizer
        self._choices = choices
        self._results = []

    def predict(self, context, random_seed=None):
        # Random seed 
        if random_seed is None:
            random_seed = get_os_random_seed()
        set_all_random_seeds(random_seed)

        inputs = self._tokenizer(
            [context] * len(self._choices),
            self._choices,
            return_tensors="pt",
            padding=True,
            truncation=True,
        )
        outputs = self._model(**{k: v.unsqueeze(0) for k,v in inputs.items()})

        detached_logits = outputs.logits.detach()
        logits = detached_logits.numpy()[0]
        self._add_result(context, random_seed, logits)

        predicted_index = outputs.logits.argmax().item()
        return self._choices[predicted_index]
    
    def _add_result(self, context, random_seed, predictions):
        result = {choice: pred for choice, pred in zip(self._choices, predictions)}
        result['context'] = context
        result['random_seed'] = random_seed
        self._results.append(result)

    def get_results(self):
        return pandas.DataFrame(self._results)[['context', 'random_seed'] + self._choices]