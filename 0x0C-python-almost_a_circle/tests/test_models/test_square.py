#!/usr/bin/python3
"""
Defines unittests for class Square

    Test classes:
        1. TestSquareInitialization
        2. TestSquareDisplayAndStr
        3. TestSquareUpdateArgsKwargs
        4. TestSquareToDictionary
        5. TestSquareArea:
"""

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


class TestSquareDisplayAndStr(unittest.TestCase):
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

    # display()
    def test_display_size(self):
        s1 = Square(3, 0, 0, 89)
        expected = '###\n###\n###\n'
        self.assertEqual(expected, self.captured_stdout(s1, 'display'))

    def test_display_size_x(self):
        s1 = Square(3, 2, 0, 89)
        expected = '  ###\n  ###\n  ###\n'
        self.assertEqual(expected, self.captured_stdout(s1, 'display'))

    def test_display_size_y(self):
        s1 = Square(3, 0, 2, 89)
        expected = '\n\n###\n###\n###\n'
        self.assertEqual(expected, self.captured_stdout(s1, 'display'))

    def test_display_size_x_y(self):
        s1 = Square(4, 2, 3, 89)
        expected = '\n\n\n  ####\n  ####\n  ####\n  ####\n'
        self.assertEqual(expected, self.captured_stdout(s1, 'display'))

    def test_display_arg_passed(self):
        with self.assertRaises(TypeError):
            Square(4, 5, 7, 89).display(1)


class TestSquareUpdateArgsKwargs(unittest.TestCase):
    """ Test cases for the update method of Square """

    # *args
    def testupdate_args_zero(self):
        s1 = Square(1, 1, 1, 1)
        s1.update()
        self.assertEqual(str(s1), '[Square] (1) 1/1 - 1')

    def test_update_args_id(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(4)
        self.assertEqual(str(s1), '[Square] (4) 1/1 - 1')

    def test_update_args_id_size(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(4, 3)
        self.assertEqual(str(s1), '[Square] (4) 1/1 - 3')

    def test_update_args_id_size_x(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(4, 1, 7)
        self.assertEqual(str(s1), '[Square] (4) 7/1 - 1')

    def test_update_args_id_size_x_y(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(4, 1, 7, 8)
        self.assertEqual(str(s1), '[Square] (4) 7/8 - 1')

    def test_update_args_exceeding(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(4, 1, 7, 8, "extra")
        self.assertEqual(str(s1), '[Square] (4) 7/8 - 1')

    def test_update_args_width_getter(self):
        s1 = Square(4, 1, 7, 8)
        s1.update(89, 2)
        self.assertEqual(2, s1.width)

    def test_update_args_height_getter(self):
        s1 = Square(4, 1, 7, 8)
        s1.update(89, 2)
        self.assertEqual(2, s1.height)

    def test_update_args_id_None(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(None)
        self.assertEqual(str(s1), f'[Square] ({s1.id}) 1/1 - 1')

    def test_udpate_args_id_None_Plus(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(None, 2, 3, 4)
        self.assertEqual(str(s1), f'[Square] ({s1.id}) 3/4 - 2')

    def test_update_args_subsequent(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(1, 2, 3, 4)
        s1.update(4, 3, 2, 1)
        self.assertEqual(str(s1), '[Square] (4) 2/1 - 3')

    def test_update_args_str_size(self):
        s1 = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s1.update(4, "size", 2, 1)

    def test_update_args_zero_size(self):
        s1 = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s1.update(4, 0, 2, 1)

    def test_update_args_size_negative(self):
        s1 = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s1.update(4, -1, 2, 1)

    def test_update_args_str_x(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(89, 1, "x")

    def test_update_args_negative_x(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(98, 1, -4)

    def test_update_args_str_y(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(89, 1, 2, "y")

    def test_update_args_negative_y(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(89, 1, "invalid", "invalid")

    # **kwargs
    def test_update_kwargs_id(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(id=4)
        self.assertEqual(str(s1), '[Square] (4) 1/1 - 1')

    def test_update_kwargs_id_size(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(size=3, id=4)
        self.assertEqual(str(s1), '[Square] (4) 1/1 - 3')

    def test_update_kwargs_id_size_x(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(id=4, size=1, x=7)
        self.assertEqual(str(s1), '[Square] (4) 7/1 - 1')

    def test_update_kwargs_id_size_x_y(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(id=4, size=1, x=7, y=8)
        self.assertEqual(str(s1), '[Square] (4) 7/8 - 1')

    def test_update_kwargs_width_getter(self):
        s1 = Square(4, 1, 7, 8)
        s1.update(id=89, size=2)
        self.assertEqual(2, s1.width)

    def test_update_kwargs_height_getter(self):
        s1 = Square(4, 1, 7, 8)
        s1.update(id=89, size=2)
        self.assertEqual(2, s1.height)

    def test_update_kwargs_id_None(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(id=None)
        self.assertEqual(str(s1), f'[Square] ({s1.id}) 1/1 - 1')

    def test_udpate_kwargs_id_None_Plus(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(id=None, size=2, x=3, y=4)
        self.assertEqual(str(s1), f'[Square] ({s1.id}) 3/4 - 2')

    def test_update_kwargs_subsequent(self):
        s1 = Square(1, 1, 1, 1)
        s1.update(id=1, size=2, x=3, y=4)
        s1.update(id=4, size=3, x=2, y=1)
        self.assertEqual(str(s1), '[Square] (4) 2/1 - 3')

    def test_update_kwargs_str_size(self):
        s1 = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s1.update(size="size")

    def test_update_kwargs_zero_size(self):
        s1 = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s1.update(size=0)

    def test_update_kwargs_size_negative(self):
        s1 = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s1.update(size=-1)

    def test_update_kwargs_str_x(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(x="x")

    def test_update_kwargs_negative_x(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(x=-4)

    def test_update_args_str_y(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(y="y")

    def test_update_args_negative_y(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(y=-4)

    def test_update_args_kwargs(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(y=1, x=1, eye_d=98, witdh=89)
        self.assertEqual(str(s1), '[Square] (10) 1/1 - 10')

    def test_update_kwargs_wrong_keys(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(eye_d=98, witdh=89)
        self.assertEqual(str(s1), '[Square] (10) 10/10 - 10')


class TestSquareToDictionary(unittest.TestCase):
    """ Test cases for the to_dictionary method of a Rectangle """
    def test_to_dictionary_type(self):
        s1 = Square(10, 2, 1, 9)
        self.assertEqual(type(s1.to_dictionary()), dict)

    def test_to_dictionary_output(self):
        s1 = Square(10, 2, 1, 9)
        expected = {'id': 9, 'x': 2, 'y': 1, 'width': 10, 'height': 10}
        self.assertEqual(type(s1.to_dictionary()), dict)

    def test_to_dictionary_after_update(self):
        s1 = Square(10, 2, 1, 9)
        kwargs = s1.to_dictionary()
        s2 = Square(5, 9, 1, 2)
        s2.update(**kwargs)
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg_passed(self):
        with self.assertRaises(TypeError):
            s1 = Square(10, 2, 1, 9)
            s1.to_dictionary(0)


class TestSquareArea(unittest.TestCase):
    """ Test cases for the area of a Rectangle """

    def test_small_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_large_area(self):
        s1 = Square(10**18)
        self.assertEqual(s1.area(), 10**36)

    def test_modified_size_area(self):
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.area(), 100)

    def test_arg_passed_to_area(self):
        r1 = Square(5)
        with self.assertRaises(TypeError):
            r1.area(2)


class TestSquareToDictionary(unittest.TestCase):
    """ Test cases for the to_dictionary method of a Square """

    def test_to_dictionary_type(self):
        s1 = Square(1, 1, 1, 1)
        self.assertEqual(type(s1.to_dictionary()), dict)

    def test_to_dictionary_output(self):
        s1 = Square(1, 2, 3, 4)
        expected = {"id": 4, "y": 3, "size": 1, "x": 2}
        self.assertEqual(expected, s1.to_dictionary())

    def test_to_dictionary_for_update(self):
        s1 = Square(1, 2, 3, 4)
        kwargs = s1.to_dictionary()
        s2 = Square(4, 3, 2, 1)
        s2.update(**kwargs)
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_one_arg_passed(self):
        with self.assertRaises(TypeError):
            r1 = Square(1, 2, 3, 4)
            r1.to_dictionary(0)


if __name__ == "__main__":
    unittest.main()
