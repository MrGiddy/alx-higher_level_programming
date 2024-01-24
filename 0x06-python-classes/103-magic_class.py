#!/usr/bin/python3
"""Contains the definition of class MagicClass"""

import math


class MagicClass:
    """Represents a circle object"""

    def __init__(self, radius=0):
        """Initialzes an instance of MagicClass

        Args:
            radius (int or float): The radius of a MagicClass object

        Raises:
            TypeError: If the provided radius is not a number
        """
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the area of a MagicClass object"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of a MagicClass object"""
        return 2 * math.pi * self.__radius
