#!/usr/bin/python3
"""Define function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerFunction(unittest.TestCase):
    def test_regular_list(self):
        # Test when the list has regular integers
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_unordered_list(self):
        # Test when the list is not in ascending order
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        # Test when the list is empty
        result = max_integer([])
        self.assertIsNone(result)

    def test_negative_numbers(self):
        # Test when the list has negative numbers
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_duplicate_max(self):
        # Test when the list has duplicate maximum values
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_single_element_list(self):
        # Test when the list has only one element
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_large_numbers(self):
        # Test when the list has large integers
        result = max_integer([999999999, 1000000000, 888888888])
        self.assertEqual(result, 1000000000)

    def test_mixed_numbers(self):
        # Test when the list has a mix of positive, negative, and zero
        result = max_integer([-5, 0, 10, -2, 7])
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
