#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()
