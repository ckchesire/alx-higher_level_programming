#!/usr/bin/python3

import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        self.assertTrue(issubclass(Square, Rectangle))

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
        expected_str = "[Square] (1) 2/3 - 10"
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

    def test_display_with_position(self):
        """Test display with position"""
        s = Square(2, 2)
        expected_output = "  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as simulate_out:
            s.display()
            self.assertEqual(simulate_out.getvalue(), expected_output)

    def test_update_with_kwargs(self):
        """Test updating attributes using **kwargs."""
        sq = Square(3, 4, 5, 6)
        sq.update(size=25, x=35, y=45, id=99)
        self.assertEqual(sq.id, 99)
        self.assertEqual(sq.width, 25)
        self.assertEqual(sq.height, 25)
        self.assertEqual(sq.x, 35)
        self.assertEqual(sq.y, 45)
