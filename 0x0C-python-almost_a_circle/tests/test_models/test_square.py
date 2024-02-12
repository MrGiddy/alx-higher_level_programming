#!/usr/bin/python3
""" Defines unittests for class Square """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
import contextlib


class TestSquareInitialization(unittest.TestCase):
    """ Test cases for class Square """

    def test_isinstance_Base(self):
        self.assertIsInstance(Square(10), Base)

    def test_isinstance_Rectangle(self):
        self.assertIsInstance(Square(10), Rectangle)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_arg_size(self):
        s1 = Square(10)
        s2 = Square(9)
        self.assertEqual(s1.id, s2.id - 1)

    def test_args_size_x(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_args_size_x_y(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 10, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_args_size_x_y_id(self):
        s1 = Square(10, 2, 2, 12)
        self.assertEqual(s1.id, 12)

    def test_exceeding_args(self):
        with self.assertRaises(TypeError):
            s1 = Square(10, 2, 2, 12, "extra")

    def test_private_size(self):
        s1 = Square(10, 2, 2, 12)
        with self.assertRaises(AttributeError):
            print(s1.__size)

    def test_getter_size(self):
        s1 = Square(10, 2, 2, 12)
        self.assertEqual(s1.size, 10)

    def test_setter_size(self):
        s1 = Square(10, 2, 2, 12)
        s1.size = 5
        self.assertEqual(s1.size, 5)

    def test_getter_width(self):
        s1 = Square(10, 2, 2, 12)
        s1.size = 5
        self.assertEqual(s1.width, 5)

    def test_getter_height(self):
        s1 = Square(10, 2, 2, 12)
        s1.size = 5
        self.assertEqual(s1.width, 5)

    def test_getter_x(self):
        s1 = Square(10, 2, 3, 12)
        self.assertEqual(s1.x, 2)

    def test_gettter_y(self):
        s1 = Square(10, 2, 3, 12)
        self.assertEqual(s1.y, 3)


class TestRectangleDisplayAndStr(unittest.TestCase):
    """ Test cases for the display and __str__ methods of class Square """

    @staticmethod
    def captured_stdout(square, method):
        captured_stdout = io.StringIO()
        with contextlib.redirect_stdout(captured_stdout):
            if method == 'display':
                square.display()
            elif method == '__str__':
                print(square)

        return captured_stdout.getvalue()

    # Test cases for __str__ method
    def test_str_size(self):
        s1 = Square(4)
        expected = f'[Square] ({s1.id}) 0/0 - 4\n'
        self.assertEqual(expected, self.captured_stdout(s1, '__str__'))

    def test_str_size_x(self):
        s1 = Square(4, 5)
        expected = f'[Square] ({s1.id}) 5/0 - 4\n'
        self.assertEqual(expected, self.captured_stdout(s1, '__str__'))

    def test_str_size_x_y(self):
        s1 = Square(4, 5, 7)
        expected = f'[Square] ({s1.id}) 5/7 - 4\n'
        self.assertEqual(expected, self.captured_stdout(s1, '__str__'))

    def test_str_size_x_y_id(self):
        s1 = Square(4, 5, 7, 89)
        expected = f'[Square] ({s1.id}) 5/7 - 4\n'
        self.assertEqual(expected, self.captured_stdout(s1, '__str__'))

    def test_str_changed_attribs(self):
        s1 = Square(4, 5, 7, 89)
        s1.width = 5
        s1.x = 13
        s1.y = 3
        expected = f'[Square] ({s1.id}) 13/3 - 5\n'
        self.assertEqual(expected, self.captured_stdout(s1, '__str__'))

    def test_str_arg_passed(self):
        s1 = Square(4, 5, 7, 89)
        with self.assertRaises(TypeError):
            s1.__str__(0)
