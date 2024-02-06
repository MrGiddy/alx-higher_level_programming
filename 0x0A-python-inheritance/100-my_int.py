#!/usr/bin/python3
"""
    Defines a class that inverts == and !=
"""


class MyInt(int):
    """
        Inherits from int and Inverts == and != operators
    """
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
