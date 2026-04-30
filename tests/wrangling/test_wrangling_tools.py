import pandas as pd

from innoprod.wrangling import wrangling_tools
from tests.pdtestcase import PdTestCase

class TestWranglingTools(PdTestCase):

    def test_replace_values(self):
        s = pd.Series(['a', 'b', 'c', 'd'])
        s = wrangling_tools.replace_values(s, 'b', 'x')
        s = wrangling_tools.replace_values(s, 'd', None)
        self.assertEqual(s, pd.Series(['a', 'x', 'c', None]))

    def test_is_non_empty(self):
        ser = pd.Series(['text', '', 'more text', 'nan', 'even more text', None])
        mask = wrangling_tools.is_non_empty(ser)
        self.assertEqual(mask.tolist(), [True, False, True, False, True, False])

    def test_remove_newlines_from_str_series(self):
        ser = pd.Series(['text', 'more\n text', None, 'even\n\n more\k text\n', ''])
        expected = pd.Series(['text', 'more text', None, 'even more\k text', ''])
        result = wrangling_tools.remove_newlines_from_str_series(ser)
        self.assertEqual(result, expected)

    def test_parse_sterling_monetary_values(self):
        ser = pd.Series(['£1,000', '£2,500.50', '-', '', None])
        expected = pd.Series([1000.0, 2500.50, None, None, None])
        result = wrangling_tools.parse_sterling_monetary_values(ser)
        self.assertEqual(result, expected)