from ..data_frame import PandaDataFrame 
from unittest.mock import patch
#>>> @patch('module.ClassName2')
#... @patch('module.ClassName1')
#... def test(MockClass1, MockClass2):
#...     module.ClassName1()
#...     module.ClassName2()
#...     assert MockClass1 is module.ClassName1
#...     assert MockClass2 is module.ClassName2
#...     assert MockClass1.called
#...     assert MockClass2.called
#...
#>>> test()