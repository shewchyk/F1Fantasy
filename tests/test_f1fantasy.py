import unittest
import unittest.mock
from unittest import mock
from f1fantasy import dr_fp1

class TestDriverList(unittest.TestCase):
    def test_dr_fp1(self):
        drivers = ["first", "second", "Third"]
        index = 0
        result = dr_fp1(drivers, index)
        self.assertEqual(result)

if __name__ == '__main__':
    unittest.main()
    
#def dr_fp1(drivers, index):
#    return [i[index] for i in drivers] 