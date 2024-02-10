#!/usr/bin/python3
"""
Defines unittests for class Rectangle of module rectangle.py

    The unittest classes:
        1. TestRectangleInitialization
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInitialization(unittest.TestCase):
    """ Test cases for class Rectangle """

    def setUp(self):
        self.r1 = Rectangle(10, 2, 0, 0, None)

    def test_inherits_from_Base(self):
        self.assertIsInstance(self.r1, Base)

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            print(self.r1.__width)

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            print(self.r1.__height)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(self.r1.__x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(self.r1.__y)

    def test_setter_width(self):
        r2 = Rectangle(2, 10, 0, 0, None)
        r2.width = 5
        self.assertEqual(r2.width, 5)

    def test_getter_width(self):
        r2 = Rectangle(2, 10, 0, 0, None)
        self.assertEqual(r2.width, 2)

    def test_setter_height(self):
        r2 = Rectangle(2, 10, 0, 0, None)
        r2.height = 5
        self.assertEqual(r2.height, 5)

    def test_getter_height(self):
        r2 = Rectangle(2, 10, 0, 0, None)
        self.assertEqual(r2.height, 10)

    def test_setter_x(self):
        r2 = Rectangle(2, 10, 0, 0)
        r2.x = 50
        self.assertEqual(r2.x, 50)

    def test_getter_x(self):
        r2 = Rectangle(2, 10, 0, 0)
        self.assertEqual(r2.x, 0)

    def test_setter_y(self):
        r2 = Rectangle(2, 10, 0, 0)
        r2.y = 50
        self.assertEqual(r2.y, 50)

    def test_getter_y(self):
        r2 = Rectangle(2, 10, 0, 0)
        self.assertEqual(r2.y, 0)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle(10)

    def test_two_args(self):
        r2 = Rectangle(10, 2)
        r3 = Rectangle(2, 10)
        self.assertEqual(r2.id, r3.id - 1)

    def test_three_args(self):
        r2 = Rectangle(10, 2, 8)
        r3 = Rectangle(2, 10, 4)
        self.assertEqual(r2.id, r3.id - 1)

    def test_four_args(self):
        r2 = Rectangle(10, 2, 8, 16)
        r3 = Rectangle(2, 10, 4, 8)
        self.assertEqual(r2.id, r3.id - 1)

    def test_five_args(self):
        r2 = Rectangle(10, 2, 8, 16, 12)
        self.assertEqual(12, r2.id)

    def test_greater_than_five_args(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 2, 0, 0, None, "extra")


class TestRectangleWidth(unittest.TestCase):
    """ Tests cases for the width attribute of a Rectangle """
    def test_width_int(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(type(r1.width), int)

    def test_width_bool(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Rectangle(True, 2)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r1 = Rectangle(-10, 2)

    def test_width_string(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Rectangle(True, 2)

    def test_width_float_inf(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Rectangle(float('inf'), 2)

    def test_width_None(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Rectangle(None, 2)

    def test_width_nan(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Rectangle(float('nan'), 2)


class TestRectangleHeight(unittest.TestCase):
    """ Tests cases for the height attribute of a Rectangle """
    def test_height_int(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(type(r1.height), int)

    def test_height_bool(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1 = Rectangle(10, False)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r1 = Rectangle(10, -2)

    def test_height_string(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1 = Rectangle(10, "rectangle")

    def test_height_float_inf(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1 = Rectangle(2, float('inf'))

    def test_height_None(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1 = Rectangle(2, None)

    def test_height_nan(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1 = Rectangle(2, float('nan'))
