import pandas as pd
from parameterized import parameterized

from innoprod.text_analysis import code_matching
from innoprod.text_analysis.matching_status import MatchingStatus
from tests.pdtestcase import PdTestCase

class TestCodeMatching(PdTestCase):

    @parameterized.expand([
            [['test'], ['this is a test'], [MatchingStatus.UNVERIFIED]],
            [['test', 'sent'], ['another sentence'], [MatchingStatus.UNVERIFIED]],
            [['test'], ['different text'], [MatchingStatus.NO_MATCH]],
            [['sent'], ['I sent a letter'], [MatchingStatus.UNVERIFIED]],
            [['test', 'sent'], ['this is a test', 'another sentence', 'different text', 'I sent a letter'], [MatchingStatus.UNVERIFIED, MatchingStatus.UNVERIFIED, MatchingStatus.NO_MATCH, MatchingStatus.UNVERIFIED]],
        ])
    def test_add_code(self, code_patterns, cleaned_sentences, expected_matches):
        # Arrange
        code_name = 'Test'
        codes_df = None # TODO test with existing codes_df as well
        recurring_sentences_df = pd.DataFrame({'Cleaned Sentence': cleaned_sentences})
        
        # Act
        updated_codes_df, updated_recurring_sentences_df = code_matching.add_code(code_name, code_patterns, codes_df, recurring_sentences_df)
        
        # Assert
        expected = pd.DataFrame({'Code': [code_name], 'Patterns': [code_patterns]})
        self.assertEqual(updated_codes_df, expected)
        
        expected = pd.DataFrame({
            'Cleaned Sentence': cleaned_sentences,
            code_name: expected_matches
        })
        self.assertEqual(updated_recurring_sentences_df, expected)


    @parameterized.expand([
            [['test'], ['this is a test'], [MatchingStatus.UNVERIFIED], [MatchingStatus.UNVERIFIED]],
            [['test'], ['different text'], [MatchingStatus.NO_MATCH], [MatchingStatus.NO_MATCH]],
            [['test', 'text'], ['different text'], [MatchingStatus.NO_MATCH], [MatchingStatus.UNVERIFIED]],
            [['test'], ['this is now broken'], [MatchingStatus.VERIFIED], [MatchingStatus.BROKEN]],
            [['test'], ['this is a test'], [MatchingStatus.VERIFIED], [MatchingStatus.VERIFIED]],
            [['sentence'], ['I sent a letter'], [MatchingStatus.INCORRECT], [MatchingStatus.VERIFIED]],
            [['text'], ['different text'], [MatchingStatus.INCORRECT], [MatchingStatus.INCORRECT]],
            [['text'], ['this is a test'], [MatchingStatus.BROKEN], [MatchingStatus.BROKEN]],
            [['test'], ['this is a test'], [MatchingStatus.BROKEN], [MatchingStatus.VERIFIED]],
        ])
    def test_modify_code(self, code_patterns, cleaned_sentences, previous_statuses, expected_matches):
        # Arrange
        code_name = 'Test'
        codes_df = pd.DataFrame({'Code': [code_name], 'Patterns': [code_patterns]})
        recurring_sentences_df = pd.DataFrame({'Cleaned Sentence': cleaned_sentences, code_name: previous_statuses})
        
        # Act
        updated_codes_df, updated_recurring_sentences_df = code_matching.modify_code(code_name, code_patterns, codes_df, recurring_sentences_df)
        
        # Assert
        expected = pd.DataFrame({'Code': [code_name], 'Patterns': [code_patterns]})
        self.assertEqual(updated_codes_df, expected)
        
        expected = pd.DataFrame({
            'Cleaned Sentence': cleaned_sentences,
            code_name: expected_matches
        })
        self.assertEqual(updated_recurring_sentences_df, expected)
