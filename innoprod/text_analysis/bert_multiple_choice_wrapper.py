import pandas
import os
import transformers

from ..random_tools import set_all_random_seeds

class BertMultipleChoiceWrapper:
    def __init__(self, model_name, choices):
        self._model_name = model_name
        self._model = transformers.BertForMultipleChoice.from_pretrained(model_name)
        self._tokenizer = transformers.BertTokenizer.from_pretrained(model_name)
        self._choices = choices
        self._results = []

    def predict(self, context, random_seed=None):
        # Random seed 
        if random_seed is None:
            random_seed = os.urandom(16)
        set_all_random_seeds(random_seed)

        inputs = self._tokenizer(
            [context] * len(self._choices),
            self._choices,
            return_tensors="pt",
            padding=True,
            truncation=True,
        )
        outputs = self._model(**{k: v.unsqueeze(0) for k,v in inputs.items()})

        self._add_result(context, random_seed, outputs.logits.detach().numpy()[0])

        predicted_index = outputs.logits.argmax().item()
        return self._choices[predicted_index]
    
    def _add_result(self, context, random_seed, predictions):
        result = {choice: pred for choice, pred in zip(self._choices, predictions)}
        result['context'] = context
        result['random_seed'] = random_seed

        self._results = self._results.append(result)

    def get_results(self):
        return pandas.DataFrame(self._results)