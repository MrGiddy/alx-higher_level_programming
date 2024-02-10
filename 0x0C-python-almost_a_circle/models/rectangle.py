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
        def width(self, width):
            """ Set/Get the width of Rectangle instance """
            return self.__width

        @width.setter
        def width(self, width):
            self.__width = width

        @property
        def height(self, height):
            """ Set/Get the height of Rectangle instance """
            return self.__height

        @height.setter
        def height(self, height):
            self.__height = height

        @property
        def x(self, x):
            """ Set/Get the x coordinate of Rectangle instance """
            return self.__x

        @x.setter
        def x(self, x):
            self.__x = x

        @property
        def y(self, y):
            """ Set/Get the y coordinate of Rectangle instance """
            return self.__y

        @y.setter
        def y(self, y):
            self.__y = y
