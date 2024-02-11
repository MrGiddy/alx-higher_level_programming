#!/usr/bin/python3
""" Defines class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """
    Blueprint for an instance of class Rectangle

    Attributes:
        Base (cls): The base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new instance of Rectangle

        Attributes:
            width (int): The width of new Rectangle
            height (int): the height of new Rectangle
            x (int): x coordinate of new Rectangle
            y (int): y coordinate of new Rectangle
            id (int): The identity of new Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Set/Get the width of Rectangle instance """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """ Set/Get the height of Rectangle instance """
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """ Set/Get the x coordinate of Rectangle instance """
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """ Set/Get the y coordinate of Rectangle instance """
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """ Print the area of a Rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints Rectangle using '#' to stdout """
        for y in range(self.y):
            print(' ')
        for h in range(self.height):
            for x in range(self.x):
                print(' ', end="")
            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ Override str to return custom Rectangle info. """
        c = self.__class__.__name__
        s = f'[{c}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'
        return s
