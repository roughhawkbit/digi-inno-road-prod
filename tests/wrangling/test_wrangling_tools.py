import unittest

import pandas as pd
import pandas.testing as pd_testing

from innoprod.wrangling import wrangling_tools

class TestPathTools(unittest.TestCase):

    def assertDataframeEqual(self, a, b, msg):
        try:
            pd_testing.assert_frame_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e

    def setUp(self):
        self.addTypeEqualityFunc(pd.DataFrame, self.assertDataframeEqual)
    
    def test_replace_values(self):
        df = pd.DataFrame({'col1': ['a', 'b', 'c', 'd'], 'col2': [1, 2, 3, 4]})
        df = wrangling_tools.replace_values(df, 'col1', 'b', 'x')
        df = wrangling_tools.replace_values(df, 'col1', 'd', None)
        self.assertEqual(df, pd.DataFrame({'col1': ['a', 'x', 'c', None], 'col2': [1, 2, 3, 4]}))

    def test_is_non_empty(self):
        ser = pd.Series(['text', '', 'more text', 'nan', 'even more text', None])
        mask = wrangling_tools.is_non_empty(ser)
        self.assertEqual(mask.tolist(), [True, False, True, False, True, False])
        
