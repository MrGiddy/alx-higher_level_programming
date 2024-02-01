#!/usr/bin/python3
""" Definition of class Rectangle """


class Rectangle:
    """ Defines class Rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle

        Args:
            width (int): Width of a new rectangle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Returns the area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)

        return (2 * (self.__height + self.__width))

    def __str__(self):
        """
        Displays rectangle using # if str() or print() is
        called on an instance of class Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        elems = []
        for i in range(self.__height):
            for j in range(self.__width):
                elems.append("#")
            elems.append('\n')
        return "".join(elems[:-1])

    def __repr__(self):
        """
        Returns a string recreateable to a new rectangle
        instance using eval
        """
        return ('Rectangle(' + f'{self.__width}'
                + ', ' + f'{self.__height}' + ')')

    def __del__(self):
        """ Deletes an instance of class Rectangle """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
