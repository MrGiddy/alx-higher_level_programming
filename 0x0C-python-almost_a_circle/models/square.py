#!/usr/bin/python3
""" Defines class Square - A special Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square

        Args:
            size (int): The size of new Square
            x (int): New Square x-coordinate
            y (int): New Square y-coordinate
            id (int): Identity of new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Set/Get size of a Square  """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ Override __str__ for print() and str() outputs """
        c = self.__class__.__name__
        s = f'[{c}] ({self.id}) {self.x}/{self.y} - {self.width}'
        return s
