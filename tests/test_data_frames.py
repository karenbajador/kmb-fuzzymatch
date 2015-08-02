

from data_frame import PandaDataFrame 
from settings import TEST_FILE
from unittest.mock import patch
import unittest
import collections






class TestDataFrame(unittest.TestCase):
    
    pd_cls = PandaDataFrame(TEST_FILE)

    def test_extract_data_from_spreadsheet(self):
        """
        Extract data from spreadsheet
        """
        self.assertEqual("Al Jaber Group LLC", self.pd_cls.df["Company Name"][8])
        
        
    def test_saves_dataframe_to_spreadsheet(self):
        """
        Saves data frame to spreadsheet
        """
        
        index = 9
        best_score = 95
        Match = collections.namedtuple("Match", ["crm_company_id", "crm_company_name", "crm_group_id"])
        best_match = Match(crm_company_id = "12345",crm_company_name = "Al Jaber Group LLC",crm_group_id = "54321")
        error = ""
        
        try:
            self.pd_cls.update_df(index, best_match, best_score)
        except Exception as e:
            error= e
            
        self.assertEqual("", error)   



if __name__ == '__main__':
    unittest.main()

