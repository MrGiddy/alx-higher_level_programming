#!/usr/bin/python3
""" Definition of class Rectangle """


class Rectangle:
    """ Defines class Rectangle """

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle

        Args:
            width (int): Width of a new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves the set width of rectangle """
        return self.__width

    @property
    def height(self):
        """ Retrieves the set height of rectangle """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets width of rectangle to value

        Args:
            value (int): The width to set for the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets height of rectangle to value

        Args:
            value (int): The height to set for the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
