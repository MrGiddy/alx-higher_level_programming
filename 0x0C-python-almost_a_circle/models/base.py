#!/usr/bin/python3
""" Defines class Base """


class Base:
    """
    Manages id attribute of its child classes

    Attributes:
        __nb_objects (int): Initializes id attribute
        of objects created without id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of base

        Attributes:
            id (int): Identity of a Base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
