#!/usr/bin/python3
"""" Unit tests for Base class """

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import mock_open, patch
import json


class BaseTestCase(unittest.TestCase):
    """ Test cases for the Base class """

    def setUp(self):
        """ To reset private class attribute __nb_objects before each test """
        Base._Base__nb_objects = 0

    def test_id_autoincrement(self):
        """ Test auto-increment"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base()
        self.assertEqual(self.b1.id, (1))
        self.assertEqual(self.b2.id, (2))
        self.assertEqual(self.b3.id, (3))
        self.assertEqual(self.b4.id, (4))

    def test_custom_Base_id(self):
        """ Test where id is provided """
        self.b = Base(14)
        self.assertEqual(self.b.id, 14)

    def test_mixed(self):
        """ Test auto and manual id assignment """
        b1 = Base(1)
        b3 = Base(49)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b3.id, 49)

    def test_negative(self):
        """ Test for negative id """
        b = Base(-10)
        self.assertEqual(b.id, -10)

    def test_none(self):
        """ Test for none """
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_multiple_none(self):
        """ Test for multiple none """
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_private_class_attr(self):
        """ Test __nb_objects private """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_to_json_string_empty_list(self):
        """ Test to_json_string with non-empty and empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file_none(self):
        """Test save_to_file with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        """Test save_to_file with empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_rectangle(self):
        """Test save_to_file with Rectangle instances"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

    def test_save_to_file_square(self):
        """Test save_to_file with Square instances"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])

    def test_from_json_string_invalid(self):
        """Test from_json_string with None input,  empty string and
            empty list
        """
        result = Base.from_json_string(None)
        self.assertEqual(result, [])
        self.assertIsInstance(result, list)

        result1 = Base.from_json_string("")
        self.assertEqual(result1, [])
        self.assertIsInstance(result1, list)

        result2 = Base.from_json_string("[]")
        self.assertEqual(result2, [])
        self.assertIsInstance(result2, list)

    def test_from_json_string(self):
        """Test from_json_string with JSON string for rectangle and square"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        result = Base.from_json_string(json_string)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], dict)
        self.assertEqual(result[0]['width'], 10)
        self.assertEqual(result[0]['height'], 7)
        self.assertEqual(result[0]['x'], 2)
        self.assertEqual(result[0]['y'], 8)

        s1 = Square(5, 1, 2)
        dictionary = s1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        result = Base.from_json_string(json_string)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], dict)
        self.assertEqual(result[0]['size'], 5)
        self.assertEqual(result[0]['x'], 1)
        self.assertEqual(result[0]['y'], 2)

    def test_create_rectangle_and_square(self):
        """Test that create method correctly creates a Rectangle and square
            instance with given attributes."""
        attrs = {"id": 10, "width": 4, "height": 6, "x": 2, "y": 3}
        r_instance = Rectangle.create(**attrs)

        self.assertIsInstance(r_instance, Rectangle)
        self.assertEqual(r_instance.id, 10)
        self.assertEqual(r_instance.width, 4)
        self.assertEqual(r_instance.height, 6)
        self.assertEqual(r_instance.x, 2)
        self.assertEqual(r_instance.y, 3)

        attrs = {"id": 15, "size": 5, "x": 1, "y": 2}
        s_instance = Square.create(**attrs)

        self.assertIsInstance(s_instance, Square)
        self.assertEqual(s_instance.id, 15)
        self.assertEqual(s_instance.size, 5)
        self.assertEqual(s_instance.width, 5)
        self.assertEqual(s_instance.height, 5)
        self.assertEqual(s_instance.x, 1)
        self.assertEqual(s_instance.y, 2)

    @patch("models.base.os.path.isfile", return_value=True)
    @patch("models.base.open", new_callable=mock_open, read_data='[{"id": 1,\
            "width": 5, "height": 5, "x": 0, "y": 0}]')
    def test_load_from_file_rectangle(self, mock_open, mock_isfile):
        """Test for Rectangle class when file is presenr and has valid data."""
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 1)
        self.assertIsInstance(rects[0], Rectangle)
        self.assertEqual(rects[0].id, 1)
        self.assertEqual(rects[0].width, 5)
        self.assertEqual(rects[0].height, 5)
        self.assertEqual(rects[0].x, 0)
        self.assertEqual(rects[0].y, 0)

    @patch("models.base.os.path.isfile", return_value=True)
    @patch("models.base.open", new_callable=mock_open, read_data='[{"id": 1, \
            "size": 3, "x": 1, "y": 1}]')
    def test_load_from_file_square(self, mock_open, mock_isfile):
        """Test for Square class when file is present and has valid data."""
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].id, 1)
        self.assertEqual(squares[0].size, 3)
        self.assertEqual(squares[0].x, 1)
        self.assertEqual(squares[0].y, 1)

    @patch("models.base.os.path.isfile", return_value=False)
    def test_load_from_file_no_file(self, mock_isfile):
        """Test for when file does is not there, should return an
            empty list.
        """
        rects = Rectangle.load_from_file()
        self.assertEqual(rects, [])

    @patch("models.base.os.path.isfile", return_value=True)
    @patch("models.base.open", new_callable=mock_open, read_data='[]')
    def test_load_from_file_empty_file(self, mock_open, mock_isfile):
        """Test for an empty JSON file, should return an empty list."""
        rects = Rectangle.load_from_file()
        self.assertEqual(rects, [])

    @patch("models.base.os.path.isfile", return_value=True)
    @patch("models.base.open", new_callable=mock_open, read_data='invalid\
            json')
    def test_load_from_file_invalid_json(self, mock_open, mock_isfile):
        """Test for invalid JSON data, should raise a JSONDecodeError."""
        with self.assertRaises(json.JSONDecodeError):
            Rectangle.load_from_file()


if __name__ == '__main__':
    unittest.main()
