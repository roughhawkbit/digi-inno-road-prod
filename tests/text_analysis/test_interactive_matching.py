import pandas
import unittest

from innoprod.text_analysis import interactive_matching
from innoprod.text_analysis.matching_status import MatchingStatus

from tests.pdtestcase import PdTestCase

class TestPathTools(PdTestCase):

    def test_verification_widget(self):
        df = pandas.DataFrame({
                'unverified sentence': MatchingStatus.UNVERIFIED,
                'no match sentence': MatchingStatus.NO_MATCH,
                'verified sentence': MatchingStatus.VERIFIED,
                'incorrect sentence': MatchingStatus.INCORRECT,
                'broken sentence': MatchingStatus.BROKEN,
            }.items(),
            columns=['Cleaned Sentence', 'Test Code']
        )
        w = interactive_matching.verification_widget(df, 'Test Code')
        self.assertEqual(set(w.options), {'unverified sentence'})
    
    def test_apply_verification(self):
        df = pandas.DataFrame({
                'unverified sentence': MatchingStatus.UNVERIFIED,
                'no match sentence': MatchingStatus.NO_MATCH,
                'verified sentence': MatchingStatus.VERIFIED,
                'incorrect sentence': MatchingStatus.INCORRECT,
                'broken sentence': MatchingStatus.BROKEN,
            }.items(),
            columns=['Cleaned Sentence', 'Test Code']
        )
        w = unittest.mock.Mock()
        w.options = ['unverified sentence']
        w.get_interact_value = lambda: ['unverified sentence']
        updated_df = interactive_matching.apply_verification(df, 'Test Code', w)
        expected_df = pandas.DataFrame({
                'unverified sentence': MatchingStatus.VERIFIED,
                'no match sentence': MatchingStatus.NO_MATCH,
                'verified sentence': MatchingStatus.VERIFIED,
                'incorrect sentence': MatchingStatus.INCORRECT,
                'broken sentence': MatchingStatus.BROKEN,
            }.items(),
            columns=['Cleaned Sentence', 'Test Code']
        )
        self.assertEqual(updated_df, expected_df)