
import unittest
from parameterized import parameterized

from collections import OrderedDict
import copy

from innoprod.text_analysis import chunking_tools

one_sentence = OrderedDict()
one_sentence['Sentence one.'] = 2

two_sentences = OrderedDict()
two_sentences['Sentence one.'] = 2
two_sentences['Sentence two.'] = 2

three_sentences = OrderedDict()
three_sentences['Sentence one.'] = 2
three_sentences['Sentence two.'] = 2
three_sentences['Sentence three.'] = 2

second_sentence = OrderedDict()
second_sentence['Sentence two.'] = 2

third_sentence = OrderedDict()
third_sentence['Sentence three.'] = 2

class TestChunkingTools(unittest.TestCase):

    @parameterized.expand([
        [copy.deepcopy(one_sentence), 3, [copy.deepcopy(one_sentence)]],
        [copy.deepcopy(two_sentences), 3, [copy.deepcopy(one_sentence), copy.deepcopy(second_sentence)]],
        [copy.deepcopy(two_sentences), 4, [copy.deepcopy(two_sentences)]],
        [copy.deepcopy(three_sentences), 4, [copy.deepcopy(two_sentences), copy.deepcopy(third_sentence)]],
        [copy.deepcopy(three_sentences), 5, [copy.deepcopy(two_sentences), copy.deepcopy(third_sentence)]],
    ])
    def test_split_token_dict(self, input_dict, max_len, expected_output):
        # Arrange
        # Act
        output = chunking_tools.split_token_dict(input_dict, max_len)
        # Assert
        self.assertEqual(output, expected_output)

    @parameterized.expand([
        ["Sentence one. Sentence two. Sentence three.", 5, ["Sentence one. Sentence two.", "Sentence three."]],
        ["Sentence one. Sentence two. Sentence three.", 4, ["Sentence one. Sentence two.", "Sentence three."]],
        ["Sentence one. Sentence two. Sentence three.", 3, ["Sentence one.", "Sentence two.", "Sentence three."]],
    ])
    def test_chunk_text_sentencewise(self, input_text, max_words, expected_output):
        # Arrange
        # Act
        output = chunking_tools.chunk_text_sentencewise(input_text, max_words)
        # Assert
        self.assertEqual(output, expected_output)

