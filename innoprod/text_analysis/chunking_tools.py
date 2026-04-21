from collections import OrderedDict
import copy
import math
from nltk.tokenize import PunktSentenceTokenizer, RegexpTokenizer


def split_token_dict(token_dict: OrderedDict, max_len: int):
  try:
    if max(token_dict.values()) > max_len:
      raise Exception(f"Largest sentence token is {max(token_dict.values())} word tokens long, greater than the permitted maximum of {max_len}.")
  except Exception as e:
    print(token_dict)
    print(e)
  if len(token_dict) < 2:
    return [token_dict]
  total_len = sum(token_dict.values())
  min_n_chunks = math.ceil(total_len / max_len)
  target_chunk_len = int(round(total_len / min_n_chunks, 0))
  new_dict = OrderedDict()
  token_dict_copy = copy.deepcopy(token_dict)
  counter = 0
  while counter < target_chunk_len:
    if next(iter(token_dict_copy.values())) + counter > max_len:
      break
    sentence, token_len = token_dict_copy.popitem(last=False)
    counter += token_len
    new_dict[sentence] = token_len
  if token_dict_copy:
    return [new_dict] + split_token_dict(token_dict_copy, max_len)
  return [new_dict]

def chunk_text_sentencewise(text, max_words):
  sent_tokenizer = PunktSentenceTokenizer()
  word_tokenizer = RegexpTokenizer(r'\w+')
  sentence_tokens = sent_tokenizer.tokenize(text)
  od = OrderedDict()
  for sentence in sentence_tokens:
    n_words = len(word_tokenizer.tokenize(sentence))
    if n_words > 0:
      od[sentence] = n_words
  new_dicts = split_token_dict(od, max_words)
  return [" ".join(list(d.keys())) for d in new_dicts]

