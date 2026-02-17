import unittest

import os.path

from innoprod import path_tools

class TestPathTools(unittest.TestCase):
    
    def test_secrets_path(self):
        path = path_tools.secrets_path()
        self.assertTrue(os.path.exists(path))
        self.assertTrue(os.path.isdir(path))
        self.assertTrue(path.endswith('secrets'))
