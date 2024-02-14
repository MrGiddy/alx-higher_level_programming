#!/usr/bin/python3
"""
Defines unittests for class Base of module base.py

    The unittest classes:
        1. TestBase_init
        2. TestBaseToJsonString
        3. TestBaseSaveToFile
        4. TestBaseFromJsonString
        5. TestBaseCreate
        6. TestBaseLoadFromFile
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase_init(unittest.TestCase):
    """ Test cases for initialization of class Base """

    def test_id_not_None(self):
        obj = Base(20)
        self.assertEqual(obj.id, 20)

#    def test_id_is_None(self):
#        obj = Base()
#        obj2 = Base()
#        self.assertEqual(obj.id, 1)
#        self.assertEqual(obj2.id, 2)

    def test_unique_id_when_id_None(self):
        obj = Base()
        obj2 = Base()
        self.assertNotEqual(obj.id, obj2.id)

#    def test_id_sequence(self):
#        obj3 = Base()
#        obj4 = Base()
#        obj5 = Base()
#        obj6 = Base(12)
#        obj7 = Base()
#        self.assertEqual(obj3.id, 3)
#        self.assertEqual(obj4.id, 4)
#        self.assertEqual(obj5.id, 5)
#        self.assertEqual(obj6.id, 12)
#        self.assertEqual(obj7.id, 6)

    def test_negative_id(self):
        obj = Base(-20)
        self.assertEqual(obj.id, -20)

    def test_string_id(self):
        obj = Base("string id")
        self.assertEqual(obj.id, "string id")

    def test_is_public_id(self):
        obj = Base(20)
        obj.id = 5
        self.assertEqual(obj.id, 5)

    def test_is_private_nb_instances(self):
        obj = Base()
        with self.assertRaises(AttributeError):
            _ = obj.__nb_instances

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_Nan_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_exceeding_args_to_base(self):
        with self.assertRaises(TypeError):
            obj = Base(20, 5)


class TestBaseToJsonString(unittest.TestCase):
    """ Test cases for to_json_string method of a Square """
    def test_to_json_string_type_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_dict_arg(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_dict_args(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_type_square(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_dict_arg(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_dict_args(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_list_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none_arg(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_exceeding_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBaseSaveToFile(unittest.TestCase):
    """ Test cases for the save_to_file() method of class Base """
    @classmethod
    def tearDown(self):
        """Cleanup - Delete files created during testing """
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_list_objs_rect_None(self):
        expected = "[]"
        Rectangle.save_to_file(list_objs=None)
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            self.assertEqual(expected, f.read())

    def test_save_to_file_list_objs_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r1])
        with open('Rectangle.json', 'r', encoding='utf-7') as f:
            self.assertEqual(53, len(f.read()))

    def test_save_to_file_list_objs_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r', encoding='utf-7') as f:
            self.assertEqual(105, len(f.read()))

    def test_save_to_file_list_objs_None_square(self):
        expected = "[]"
        Square.save_to_file(list_objs=None)
        with open('Square.json', 'r', encoding='utf-8') as f:
            self.assertEqual(expected, f.read())

    def test_save_to_file_list_objs_square(self):
        s1 = Square(10, 7, 2, 8)
        Square.save_to_file([s1])
        with open('Square.json', 'r', encoding='utf-7') as f:
            self.assertEqual(39, len(f.read()))

    def test_save_to_file_list_objs_rectangles(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Rectangle.save_to_file([s1, s2])
        with open('Rectangle.json', 'r', encoding='utf-7') as f:
            self.assertEqual(77, len(f.read()))

    def test_save_to_file_filename_is_Base(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwritten(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_list_objs_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args_square(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_no_args_rectangle(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


class TestBaseFromJsonString(unittest.TestCase):
    """ Test cases for from_json_string() method of Base """
    def test_from_json_string_empty_list(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_None(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_is_type_list(self):
        dict_lst_in = [{"id": 89, "width": 10, "height": 4}]
        json_string = Rectangle.to_json_string(dict_lst_in)
        dict_lst_out = Rectangle.from_json_string(json_string)
        self.assertEqual(list, type(dict_lst_out))

    def test_from_json_string_to_rectangle(self):
        dict_lst_in = [
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_string = Rectangle.to_json_string(dict_lst_in)
        dict_lst_out = Rectangle.from_json_string(json_string)
        self.assertEqual(dict_lst_in, dict_lst_out)

    def test_from_json_string_to_rectangles(self):
        dicts_lst_in = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_string = Rectangle.to_json_string(dicts_lst_in)
        dicts_lst_out = Rectangle.from_json_string(json_string)
        self.assertEqual(dicts_lst_in, dicts_lst_out)

    def test_from_json_string_to_square(self):
        dict_lst_in = [
            {"id": 89, "size": 10, "height": 4},
        ]
        json_string = Square.to_json_string(dict_lst_in)
        dict_lst_out = Square.from_json_string(json_string)
        self.assertEqual(dict_lst_in, dict_lst_out)

    def test_from_json_string_to_squares(self):
        dicts_lst_in = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7},
        ]
        json_string = Square.to_json_string(dicts_lst_in)
        dicts_lst_out = Square.from_json_string(json_string)
        self.assertEqual(dicts_lst_in, dicts_lst_out)

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_exceeding_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(1, [])


class TestBaseCreate(unittest.TestCase):
    """ Test cases for create() method of Base class  """
    def test_create_rectangle_same_output(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_not_same_object(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_not_equal_objects(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_same_output(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_not_same_object(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_not_equal_objects(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBaseLoadFromFile(unittest.TestCase):
    """ Test cases for method load_from_file of Base """
    def tearDown(self):
        """ Cleanup - Delete files created"""
        try:
            os.remove('Rectangle.json')
        except FileNotFoundError:
            pass

        try:
            os.remove("Squre.json")
        except FileNotFoundError:
            pass

    def test_load_from_file_list_type(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        self.assertEqual(type(Rectangle.load_from_file()), list)
        s1 = Square(5)
        Square.save_to_file([s1])
        self.assertEqual(type(Square.load_from_file()), list)

    def test_load_from_file_empty_list(self):
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_empty_file(self):
        Rectangle.save_to_file("")
        self.assertEqual(Rectangle.load_from_file(), [])
        Square.save_to_file("")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_dne_rectangle(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_dne_square(self):
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_square(self):
        s1 = Square(5, 4, 3, 2)
        Square.save_to_file([s1])
        lst = Square.load_from_file()
        self.assertEqual(str(lst[0]), str(s1))
        self.assertTrue(type(lst[0]) == type(s1))

    def test_load_from_file_squares(self):
        s1 = Square(5, 4, 3, 2)
        s2 = Square(1, 2, 3, 4)
        Square.save_to_file([s1, s2])
        lst = Square.load_from_file()
        self.assertEqual(str(lst[0]), str(s1))
        self.assertEqual(str(lst[1]), str(s2))

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        lst = Rectangle.load_from_file()
        self.assertEqual(str(lst[0]), str(r1))
        self.assertTrue(type(lst[0]) == type(r1))

    def test_load_from_file_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(8, 2, 7, 10)
        Rectangle.save_to_file([r1, r2])
        lst = Rectangle.load_from_file()
        self.assertEqual(str(lst[0]), str(r1))
        self.assertEqual(str(lst[1]), str(r2))

    def test_load_from_file_two_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBaseSaveToFileCsv(unittest.TestCase):
    """ Test cases for save_to_file_csv method of class Base  """
    @classmethod
    def tearDown(self):
        """ Cleanup - Delete files created for test cases """
        try:
            os.remove('Rectangle.csv')
        except FileNotFoundError:
            pass

        try:
            os.remove('Square.csv')
        except FileNotFoundError:
            pass

        try:
            os.remove('Base.csv')
        except FileNotFoundError:
            pass

    def test_save_to_file_csv_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 3)
        Rectangle.save_to_file_csv([r1])
        with open('Rectangle.csv', 'r') as f:
            self.assertEqual(f.read().strip(), '3,10,7,2,8')

    def test_save_to_file_csv_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 3)
        r2 = Rectangle(3, 8, 7, 2, 10)
        Rectangle.save_to_file_csv([r1, r2])
        with open('Rectangle.csv', 'r') as f:
            self.assertEqual('3,10,7,2,8', f.readline().strip())
            self.assertEqual('10,3,8,7,2', f.readline().strip())

    def test_save_to_file_csv_square(self):
        s1 = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s1])
        with open("Square.csv", "r") as f:
            self.assertEqual("8,10,7,2", f.read().strip())

    def test_save_to_file_csv_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 2, 7, 10)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertEqual('8,10,7,2', f.readline().strip())
            self.assertEqual('10,8,2,7', f.readline().strip())

#    def test_save_to_file_csv_filename_Base(self):
#        s1 = Square(10, 7, 2, 8)
#        Base.save_to_file_csv([s1])
#        with open("Base.csv", "r") as f:
#            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwritten(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args_passed(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_csv_exceeding_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 0)


if __name__ == "__main__":
    unittest.main()
