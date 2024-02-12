#!/usr/bin/python3
"""
Defines unittests for class Base of module base.py

    The unittest classes:
        1. TestBase_init
        2. TestBaseToJsonString
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_init(unittest.TestCase):
    """ Test cases for initialization of class Base """

    def test_id_not_None(self):
        obj = Base(20)
        self.assertEqual(obj.id, 20)

    def test_id_is_None(self):
        obj = Base()
        obj2 = Base()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_unique_id_when_id_None(self):
        obj = Base()
        obj2 = Base()
        self.assertNotEqual(obj.id, obj2.id)

    def test_id_sequence(self):
        obj3 = Base()
        obj4 = Base()
        obj5 = Base()
        obj6 = Base(12)
        obj7 = Base()
        self.assertEqual(obj3.id, 3)
        self.assertEqual(obj4.id, 4)
        self.assertEqual(obj5.id, 5)
        self.assertEqual(obj6.id, 12)
        self.assertEqual(obj7.id, 6)

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


if __name__ == "__main__":
    unittest.main()
