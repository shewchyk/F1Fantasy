import unittest
import unittest.mock
from unittest.mock import patch
from class_driverinfo import sprint
import pytest

@pytest.fixture
def driver_index_b():
    return sprint(0, ["Driver A", "Driver B"])

#Sprint test
def test_fp_sprint(driver_index_b):
    driver_index_b.fp_sprint()
    input = mock_user_input()

    def mock_user_input():
        return '5 5 5'


#if __name__ == '__main__':
#    unittest.main()  