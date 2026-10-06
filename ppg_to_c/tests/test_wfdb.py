import unittest
from package.PPGReader import *
import sys

class Testwfdb(unittest.TestCase):
    def test_imports_wfdb(self):
        isLoaded = False
        if 'wfdb' in sys.modules:
            isLoaded = True
        self.assertTrue(isLoaded)
        

if __name__ == "__main__":
    unittest.main()