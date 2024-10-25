#!/usr/bin/python3
"""" Unit tests for Base class """

import unittest
from models.base import Base


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


if __name__ == '__main__':
    unittest.main()
