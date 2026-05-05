import unittest

import numpy
import random

from innoprod import random_tools

class TestRandomTools(unittest.TestCase):

    def test_set_all_random_seeds(self):
        # Arrange
        random_tools.set_all_random_seeds(42)

        # Act 
        numpy_int = numpy.random.randint(0, 100)
        random_int = random.randint(0, 100)
        
        # tranformers does not have its own random number generator 
        # but instead relies on those of other packages.

        # Do not test for torch random number generators here, until after it
        # it established how to run unit tests within Goolge Colab.

        # Assert
        self.assertEqual(numpy_int, 51)
        self.assertEqual(random_int, 81)