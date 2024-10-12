#!/usr/bin/python3
""" Module covers unittest for max_integer """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class defines unittests for max_integer() function"""

    def test_max_at_end(self):
        """Test max integer with sorted list."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)

    def test_max_in_middle(self):
        """Test when max integer unorderd  list."""
        self.assertEqual(max_integer([1, 7, 3, 4, 2]), 7)

    def test_one_element(self):
        """Test a list with only one element."""
        self.assertEqual(max_integer([3]), 3)

    def test_non_int(self):
        """Test a list with non-ints"""
        self.assertRaises(TypeError, max_integer, ['a', 'b', 3])

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3, -4]), -1)

    def test_mixed_sign_numbers(self):
        """Test a list with mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_all_same(self):
        """Test when all numbers in the list are the same."""
        self.assertEqual(max_integer([9, 9, 9, 9]), 9)

    def test_floats(self):
        """Test a list containing float numbers."""
        self.assertEqual(max_integer([1.0, 2.7, 3.8, 4.5]), 4.5)

    def test_mixed_floats_and_integers(self):
        """Test a list with both floats and integers."""
        self.assertEqual(max_integer([1, 2.9, 3, 4.7]), 4.7)

    def test_string_input(self):
        """Test a list with string inputs (characters)."""
        self.assertEqual(max_integer("hello"), 'o')

    def test_list_of_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["apple", "banana", "pear"]), "pear")

    def test_none_input(self):
        """Test when None is passed as input."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_list_input(self):
        """Test when a non-list input is given."""
        with self.assertRaises(TypeError):
            max_integer(11)


if __name__ == "__main__":
    unittest.main()
