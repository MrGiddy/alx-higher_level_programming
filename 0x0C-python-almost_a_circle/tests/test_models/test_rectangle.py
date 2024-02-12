#!/usr/bin/python3
"""
Defines unittests for class Rectangle of module rectangle.py

    The unittest classes:
        1. TestRectangleInitialization
        2. TestRectangleWidth
        3. TestRectangleHeight
        4. TestRectangleXCoordinate
        5. TestRectangleYCoordinate
        6. TestRectangleDisplayAndStr
        7. TestRectangleUpdate
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import contextlib


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


class TestRectangleXCoordinate(unittest.TestCase):
    """ Test the x-coordinate of new Rectangle """

    def test_x_int(self):
        r1 = Rectangle(10, 2, 7, 0, None)
        self.assertEqual(r1.x, 7)

    def test_x_bool(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r1 = Rectangle(10, 2, True, 0, None)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r1 = Rectangle(10, 2, -7, 0, None)

    def test_x_zero(self):
        r1 = Rectangle(10, 2, 0, 0, None)
        self.assertEqual(r1.x, 0)

    def test_x_string(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r1 = Rectangle(10, 2, "zero", 0, None)

    def test_x_None(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r1 = Rectangle(10, 2, None, 0, None)

    def test_x_float_nan(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r1 = Rectangle(10, 2, float('nan'), 0, None)

    def test_x_float_inf(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r1 = Rectangle(10, 2, float('inf'), 0, None)

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r1 = Rectangle(10, 2, 3.3, 0, None)


class TestRectangleYCoordinate(unittest.TestCase):
    """ Test the y-coordinate of new Rectangle """

    def test_y_int(self):
        r1 = Rectangle(10, 2, 0, 7, None)
        self.assertEqual(r1.y, 7)

    def test_y_bool(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r1 = Rectangle(10, 2, 0, True, None)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r1 = Rectangle(10, 2, 0, -7, None)

    def test_y_zero(self):
        r1 = Rectangle(10, 2, 0, 0, None)
        self.assertEqual(r1.y, 0)

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r1 = Rectangle(10, 2, 0, "zero", None)

    def test_y_None(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r1 = Rectangle(10, 2, 0, None, None)

    def test_y_float_nan(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r1 = Rectangle(10, 2, 0, float('nan'), None)

    def test_y_float_inf(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r1 = Rectangle(10, 2, 0, float('inf'), None)

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r1 = Rectangle(10, 2, 0, 3.3, None)


class TestRectangleArea(unittest.TestCase):
    """ Test cases for the area of a Rectangle """

    def test_small_area(self):
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)

    def test_large_area(self):
        r1 = Rectangle(10**18, 10**18, 0, 0, 1)
        self.assertEqual(r1.area(), 10**36)

    def test_modified_attribs_area(self):
        r1 = Rectangle(5, 10)
        r1.width = 10
        r1.height = 15
        self.assertEqual(r1.area(), 150)

    def test_arg_passed_to_area(self):
        r1 = Rectangle(5, 10, 2, 2, 2)
        with self.assertRaises(TypeError):
            r1.area(2)


class TestRectangleDisplayAndStr(unittest.TestCase):
    """ Test cases for the display and __str__ methods of class Rectangle """

    @staticmethod
    def captured_stdout(rectangle, method):
        captured_stdout = io.StringIO()
        with contextlib.redirect_stdout(captured_stdout):
            if method == 'display':
                rectangle.display()
            elif method == '__str__':
                print(rectangle)

        return captured_stdout.getvalue()

    # Test cases for display method
    def test_display_rectangle_4x3(self):
        r1 = Rectangle(4, 3)
        expected = "####\n####\n####\n"
        self.assertEqual(expected, self.captured_stdout(r1, 'display'))

    def test_display_rectangle_4x4(self):
        r1 = Rectangle(4, 4)
        expected = "####\n####\n####\n####\n"
        self.assertEqual(expected, self.captured_stdout(r1, 'display'))

    def test_display_rectangle_4x6(self):
        r1 = Rectangle(4, 6)
        expected = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(expected, self.captured_stdout(r1, 'display'))

    def test_display_width_height_x(self):
        r1 = Rectangle(4, 6, 1)
        expected = " ####\n ####\n ####\n ####\n ####\n ####\n"
        self.assertEqual(expected, self.captured_stdout(r1, 'display'))

    def test_display_width_height_y(self):
        r1 = Rectangle(4, 6, 0, 1)
        expected = "\n####\n####\n####\n####\n####\n####\n"
        self.assertEqual(expected, self.captured_stdout(r1, 'display'))

    def test_display_width_height_x_y(self):
        r1 = Rectangle(4, 6, 1, 1)
        expected = "\n ####\n ####\n ####\n ####\n ####\n ####\n"
        self.assertEqual(expected, self.captured_stdout(r1, 'display'))

    def test_display_arg_passed(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 6, 1, 1)
            r1.display(1)

    # Test cases for __str__ method
    def test_str_width_height(self):
        r1 = Rectangle(4, 5)
        cl = Rectangle.__name__
        expected = f'[{cl}] ({r1.id}) {r1.x}/{r1.y} - {r1.width}/{r1.height}\n'
        self.assertEqual(expected, self.captured_stdout(r1, '__str__'))

    def test_str_width_height_x_y(self):
        r1 = Rectangle(4, 5, 1, 1)
        cl = Rectangle.__name__
        expected = f'[{cl}] ({r1.id}) {r1.x}/{r1.y} - {r1.width}/{r1.height}\n'
        self.assertEqual(expected, self.captured_stdout(r1, '__str__'))

    def test_str_width_height_x_y_id(self):
        r1 = Rectangle(4, 5, 1, 1, 12)
        cl = Rectangle.__name__
        expected = f'[{cl}] ({r1.id}) {r1.x}/{r1.y} - {r1.width}/{r1.height}\n'
        self.assertEqual(expected, self.captured_stdout(r1, '__str__'))

    def test_str_width_height_x(self):
        r1 = Rectangle(4, 5, 1)
        cl = Rectangle.__name__
        expected = f'[{cl}] ({r1.id}) {r1.x}/{r1.y} - {r1.width}/{r1.height}\n'
        self.assertEqual(expected, self.captured_stdout(r1, '__str__'))

    def test_str_changed_attribs(self):
        r1 = Rectangle(4, 5, 1)
        r1.width = 10
        r1.height = 2
        cl = Rectangle.__name__
        expected = f'[{cl}] ({r1.id}) {r1.x}/{r1.y} - {r1.width}/{r1.height}\n'
        self.assertEqual(expected, self.captured_stdout(r1, '__str__'))

    def test_str_arg_passed(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 5, 0, 0, 12)
            r1.__str__(1)


class TestRectangleUpdate(unittest.TestCase):
    """ Test cases for update method of Rectangle """

    # *args
    def test_update_no_args(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update()
        self.assertEqual(str(r1), '[Rectangle] (10) 10/10 - 10/10')

    def test_update_id_only(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')

    def test_update_id_width(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/10')

    def test_update_id_width_height(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/3')

    def test_update_id_width_height_x(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/10 - 2/3')

    def test_update_id_width_height_x_y(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/5 - 2/3')

    def test_update_exceeding_args(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/5 - 2/3')

    def test_update_id_None(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(None)
        expected = '[Rectangle] ({}) 10/10 - 10/10'.format(r1.id)
        self.assertEqual(str(r1), expected)

    def test_update_id_None_plus(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(None, 2, 3, 4, 5, 6)
        expected = '[Rectangle] ({}) 4/5 - 2/3'.format(r1.id)
        self.assertEqual(str(r1), expected)

    def test_update_subsequent(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5, 6)
        r1.update(6, 5, 4, 3, 2, 89)
        self.assertEqual(str(r1), '[Rectangle] (6) 3/2 - 5/4')

    # **kwargs
    def test_update_kwargs_id(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(id=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_kwargs_id_width(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(id=1, width=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 2/10")

    def test_update_kwargs_id_width_height(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(width=2, height=2, id=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 2/2")

    def test_update_kwargs_id_width_height_x(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(x=0, width=2, height=2, id=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/10 - 2/2")

    def test_update_kwargs_id_width_height_x_y(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(x=0, width=2, y=3, height=2, id=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/3 - 2/2")

    def test_update_kwargs_id_None(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(id=None)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 1/1 - 1/1")

    def test_update_kwargs_id_None_Plus(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(id=None, y=3, width=8)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 10/3 - 8/10")

    def test_update_kwargs_subsequent(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(id=None, y=3, width=8)
        r1.update(id=2, y=1, width=3)
        self.assertEqual(str(r1), f"[Rectangle] (2) 10/1 - 3/10")

    def test_update_kwargs_str_width(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(id=2, y=1, width="width")

    def test_update_kwargs_negative_width(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(id=2, y=1, width=-3)

    def test_update_kwargs_float_height(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(id=2, y=1, height=3.0)

    def test_update_kwargs_negative_height(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(id=2, y=1, height=-10)

    def test_update_kwargs_bool_x(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(id=2, x=True, height=3)

    def test_update_kwargs_negative_x(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(id=2, x=-1, height=10)

    def test_update_kwargs_list_y(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(id=2, y=False, height=3)

    def test_update_kwargs_negative_y(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(id=2, y=-1, height=10)

    def test_update_args_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, width=3, y=6)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/10')

    def test_update_wrong_keys(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(id=89, hait=2, wdh=3, y=6)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/6 - 10/10')


class TestRectangleToDictionary(unittest.TestCase):
    """ Test cases for the to_dictionary method of a Rectangle """
    def test_to_dictionary_type(self):
        r1 = Rectangle(10, 2, 1, 9, None)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_to_dictionary_output(self):
        r1 = Rectangle(10, 2, 1, 9, None)
        expected = {'id': None, 'x': 1, 'y': 9, 'width': 10, 'height': 2}
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_to_dictionary_for_update(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        kwargs = r1.to_dictionary()
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**kwargs)
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg_passed(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 1, 9, None)
            r1.to_dictionary(0)


if __name__ == "__main__":
    unittest.main()
