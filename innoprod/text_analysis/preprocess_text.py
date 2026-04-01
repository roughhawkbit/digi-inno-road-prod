'''
This module contains functions for preprocessing text data, including tokenization, stop word removal, and lemmatization.
It largely follows the steps recommended in Algorithm 1 of the paper "An NLP-based approach to assessing a company's maturity level in the digital era" (2024) by Romano, Sperlì, and Vignali: https://www.sciencedirect.com/science/article/pii/S0957417424011588
These functions are essential for preparing text data for analysis and modeling in natural language processing (NLP) tasks.
'''

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

stops = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

phrases = [
    "industry 4\\.0",
]
regexpr = "|".join(phrases) + "|[\\w']+"
tokenizer = RegexpTokenizer(regexpr)

def preprocess_text(text):
    answer = remove_redactions(text)
    # Skipped as tokenization already removes punctuation.
    # answer = remove_punctuation(answer)
    answer = to_lowercase(answer)
    tokenized_answer = tokenize(answer)
    lemmatized_answer = [lemmatizer.lemmatize(word) for word in tokenized_answer]
    final_answer = remove_stop_words(lemmatized_answer)
    return final_answer


def remove_redactions(text: str) -> str:
    cleaned_text = text.replace("[REDACTED]", "")
    return cleaned_text


# def remove_punctuation(text: str) -> str:
#     return text


def to_lowercase(text: str) -> str:
    cleaned_text = text.lower()
    return cleaned_text


def tokenize(text: str) -> list:
    tokenized_text = tokenizer.tokenize(text)
    return tokenized_text


def remove_stop_words(text: list) -> list:
    final_answer = [word for word in text if word not in stops]
    return final_answer