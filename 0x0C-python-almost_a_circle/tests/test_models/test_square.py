#!/usr/bin/bash
""" Defines unittests for class Square """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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
