#!/usr/bin/python3
""" Defines class Base """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation
        of a list of dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write a JSON string representation of a list of objects
        to a file

        Args:
            list_objs (list): A list of objects
            cls (type): class
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_lst = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(dict_lst)
                f.write(json_string)
