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

    def update(self, *args, **kwargs):
        """
        Assigns arguments to Square attributes

        Args:
            *args (tuple): New values for attributes
                - args[0] - id attribute
                - args[1] - size attribute
                - args[2] = x attribute
                - args[3] = y attribute
            **kwargs (dict): New Key/Value pairs for attributes
        """

        args_lst = ["id", "size", "x", "y"]

        if args and len(args) != 0:
            for arg_name, arg_value in zip(args_lst, args):
                if arg_name == 'id':
                    if arg_value is None:
                        # Trigger super class to increment id
                        self.__init__(self.size, self.x, self.y,)
                    else:
                        setattr(self, arg_name, arg_value)
                else:
                    setattr(self, arg_name, arg_value)
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        # Trigger super class to increment id
                        self.__init__(self.size, self.x, self.y,)
                    else:
                        setattr(self, key, value)
                else:
                    setattr(self, key, value)
