from innoprod.env_tools import is_in_google_colab

import unittest

class TestEnvTools(unittest.TestCase):

    def test_is_in_google_colab(self):
        '''Tests are invariably run on a local machine, so this should always return False.'''
        # Act
        result = is_in_google_colab()

        # Assert
        self.assertFalse(result)
