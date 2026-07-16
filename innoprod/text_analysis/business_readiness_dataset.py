import torch
from torch.utils.data import Dataset

class BusinessReadinessDataset(Dataset):
    """
    Custom Dataset to handle 7 separate text responses per firm
    and map them to a continuous readiness score.
    """
    def __init__(self, dataframe, tokenizer, max_length, key_questions, drs_col):
        self.dataframe = dataframe
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.key_questions = key_questions
        self.drs_col = drs_col

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        row = self.dataframe.iloc[idx]

        # Extract the 7 text responses for this specific firm
        texts = [str(row[col]) for col in self.key_questions]

        # Tokenize the 7 texts simultaneously
        # batch_encode_plus processes a list of strings and returns stacked tensors
        encodings = self.tokenizer( #.batch_encode_plus
            texts,
            add_special_tokens=True,    # Adds [CLS] and [SEP]
            max_length=self.max_length, # Truncates or pads to this length
            padding="max_length",
            truncation=True,
            return_attention_mask=True,
            return_tensors="pt"         # Returns PyTorch tensors
        )

        # encodings['input_ids'] will automatically be shape (7, max_length)
        input_ids = encodings['input_ids']
        attention_mask = encodings['attention_mask']

        # Extract the target score and convert it to a float tensor
        # We use float because we are treating this as a regression task (MSELoss)
        label = torch.tensor(row[self.drs_col], dtype=torch.float)

        return input_ids, attention_mask, label
