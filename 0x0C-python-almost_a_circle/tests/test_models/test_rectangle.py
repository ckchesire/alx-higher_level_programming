#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """ Test case for the Rectangle class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """ Test for inheritance """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_for_constructor(self):
        """Test constructor with different combinations of arguments"""
        with self.assertRaises(TypeError):
            r = Rectangle()

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10, 1, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 12)

    def test_private_attributes(self):
        """Test for attributes that are private"""
        r = Rectangle(10, 7)

        with self.assertRaises(AttributeError):
            print(r.__width)
        with self.assertRaises(AttributeError):
            print(r.__height)
        with self.assertRaises(AttributeError):
            print(r.__x)
        with self.assertRaises(AttributeError):
            print(r.__y)

    def test_getters_setters(self):
        """Test for getter and setter methods"""
        r = Rectangle(10, 2)

        r.width = 5
        self.assertEqual(r.width, 5)

        r.height = 7
        self.assertEqual(r.height, 7)

        r.x = 9
        self.assertEqual(r.x, 9)

        r.y = 13
        self.assertEqual(r.y, 13)

    def test_invalid_attributes(self):
        """Test for validation of setter methods"""
        r = Rectangle(10, 2)

        with self.assertRaises(TypeError):
            r.width = "inv"
        with self.assertRaises(ValueError):
            r.width = 0
        with self.assertRaises(ValueError):
            r.width = -5

        with self.assertRaises(TypeError):
            r.height = "inv"
        with self.assertRaises(ValueError):
            r.height = 0
        with self.assertRaises(ValueError):
            r.height = -5

        with self.assertRaises(TypeError):
            r.x = "inv"
        with self.assertRaises(ValueError):
            r.x = -5

        with self.assertRaises(TypeError):
            r.y = "inv"
        with self.assertRaises(ValueError):
            r.y = -5

    def test_constructor_validation(self):
        """Test validation in constructor"""
        with self.assertRaises(TypeError):
            Rectangle("inv", 3)
        with self.assertRaises(TypeError):
            Rectangle(3, "inv")
        with self.assertRaises(TypeError):
            Rectangle(3, 3, "inv")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 0, "inv")

        with self.assertRaises(ValueError):
            Rectangle(0, 3)
        with self.assertRaises(ValueError):
            Rectangle(3, 0)
        with self.assertRaises(ValueError):
            Rectangle(-3, 2)
        with self.assertRaises(ValueError):
            Rectangle(2, -3)
        with self.assertRaises(ValueError):
            Rectangle(2, 2, -5)
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 0, -4)

    def test_area(self):
        """ Test for area function """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_area_large_nos(self):
        """ Test area function with large numbers """
        r = Rectangle(99999999999, 99999999999)
        self.assertEqual(r.area(), 99999999999 * 99999999999)

    def test_area_changed_values(self):
        """ Test area with changed attributes"""
        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)

        r.width = 9
        self.assertEqual(r.area(), 90)

        r.height = 4
        self.assertEqual(r.area(), 36)

    def test_area_func_exists(self):
        """ Test that the area method exists"""
        r = Rectangle(4, 2)
        self.assertTrue(hasattr(r, 'area'))
        self.assertTrue(callable(getattr(r, 'area')))

    def test_area_no_args(self):
        """ Test that area method doesn't accept arguments"""
        r = Rectangle(5, 4)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_display(self):
        """ Test displaying of a rectangle """
        r = Rectangle(3, 6)
        expected_output = '###\n###\n###\n###\n###\n###\n'
        with patch('sys.stdout', new=StringIO()) as simulated_out:
            r.display()
            self.assertEqual(simulated_out.getvalue(), expected_output)

    def test_display_exists(self):
        """ Test display method exists """
        r = Rectangle(5, 6)
        self.assertTrue(hasattr(r, 'display'))
        self.assertTrue(callable(getattr(r, 'display')))

    def test_display_no_args(self):
        """ Test display method that it should not accept arguments """
        r = Rectangle(3, 6)
        with self.assertRaises(TypeError):
            r.display(5)


if __name__ == '__main__':
    unittest.main()
