import unittest
import unittest.mock
from unittest import mock
from driverinfo import fp_sprint

class TestFpPoints(unittest.TestCase):
    def test_fp_sprint(self):
        mock_list = mock.MagicMock()
        mock_list.execute = mock.MagicMock(return_value = ["driver"])
        self.fp_sprint(0, mock_list)
        assert fp_sprint == list
       

if __name__ == '__main__':
    unittest.main()
"""
def fp_sprint(driver_index, list):
    print("Enter FP finishing positions for", str(list[driver_index][0]))
    fp1 = [int(x) for x in input().split()]
    fp_point_by_session = list[driver_index].extend(fp1) 
    return fp_point_by_session
"""