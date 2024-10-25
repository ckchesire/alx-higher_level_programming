#!/usr/bin/python3

import unittest
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    def test_square_initialization(self):
        """ Test valid initialization """
        with self.assertRaises(TypeError):
            sq = Square()

        sq = Square(10, 2, 3, 1)
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.width, 10)
        self.assertEqual(sq.height, 10)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)
        self.assertEqual(sq.id, 1)

    def test_square_str(self):
        """Test the __str__ method output of Square."""
        sq = Square(10, 2, 3, 1)
        expected_str = "[Square] (1) 2/3 - 10/10"
        self.assertEqual(str(sq), expected_str)

    def test_square_area(self):
        """Test the area method inherited from Rectangle."""
        sq = Square(10, 2, 3, 1)
        self.assertEqual(sq.area(), 100)

    def test_square_size_setter(self):
        """Test that the size setter updates width and height equally."""
        sq = Square(15, 2, 3, 1)
        self.assertEqual(sq.width, 15)
        self.assertEqual(sq.height, 15)
