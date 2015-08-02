import unittest
from fuzzy import *

class TestFuzzy(unittest.TestCase):
    


    def test_clean_company_name(self):
        """
        Extract data from spreadsheet
        """
        self.assertEqual("x", "x")
        self.assertEqual("x", "x")
        self.assertEqual("x", "ccc")
        self.assertEqual("x", "x")
        
    def test_ignore_words(self):
        """
        Extract data from spreadsheet
        """
        self.assertEqual("x", "x")
        self.assertEqual("x", "y")
        self.assertEqual("x", "x")
        self.assertEqual("x", "x")
        
    def test_fuzzy_match(self):
        """
        Extract data from spreadsheet
        """
        self.assertEqual("x", "x")        
        
        
if __name__ == '__main__':
    unittest.main()