#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TextMaxInteger(unittest.TestCase):
    """ Defines unittests for max_integer([...]) function """
    def test_empty_list(self):
        """ Tests an empty list """
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """ Tests a list with a single int element """
        self.assertEqual(max_integer([4]), 4)

    def test_sorted_list(self):
        """ Tests a sorted list of integers """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-5, -1.3, 2.6, 4]), 4)

    def test_unsorted_list(self):
        """ Tests an unsorted list of floats/ints """
        self.assertEqual(max_integer([-1, -4, 3, 2]), 3)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([4, -5, 2.6, -1.3]), 4)

    def test_list_of_floats(self):
        """ Tests lists of floats """
        self.assertEqual(max_integer([1.3, 4.6, 4.9, 2.3]), 4.9)
        self.assertEqual(max_integer([1.3, 4.6, -4.9, 2.3]), 4.6)

    def test_arg_string(self):
        """ Tests when a string is passed as an argument """
        self.assertEqual(max_integer("integer"), 't')

    def test_list_of_strings(self):
        """ Tests a list of strings """
        self.assertEqual(max_integer(["My", "name", "is", "Mr"]), "name")

    def test_repeated_element(self):
        """ Tests elements appearing more than once in list """
        self.assertEqual(max_integer([1, 4, 4, 2.3]), 4)
        self.assertEqual(max_integer([2.3, 2.3, 2.3, 2.3]), 2.3)
        self.assertEqual(max_integer(["name", "name", "name", "name"]), "name")


if __name__ == '__main__':
    unittest.main()
