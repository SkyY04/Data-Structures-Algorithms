import unittest
from lab2 import factorial, linear_search, binary_search

class Lab2TestCase(unittest.TestCase):
    """Custom test cases for lab2 functions"""

    def test_linear_search_custom(self):
        sample = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0]
        # Searching for values not in the list
        self.assertEqual(linear_search(sample, 100), -1)
        self.assertEqual(linear_search(sample, -1), -1)
        # Searching for existing values
        for idx, val in enumerate(sample):
            self.assertEqual(linear_search(sample, val), idx)

    def test_factorial_custom(self):
        # Small inputs
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        # Larger input
        self.assertEqual(factorial(10), 3628800)

    def test_binary_search_custom(self):
        sorted_list = list(range(0, 101, 5))  # [0, 5, 10, ..., 100]
        # Values that should not be found
        self.assertEqual(binary_search(sorted_list, -10), -1)
        self.assertEqual(binary_search(sorted_list, 3), -1)
        self.assertEqual(binary_search(sorted_list, 102), -1)
        # Values that should be found
        for index, value in enumerate(sorted_list):
            self.assertEqual(binary_search(sorted_list, value), index)

if __name__ == '__main__':
    unittest.main()
