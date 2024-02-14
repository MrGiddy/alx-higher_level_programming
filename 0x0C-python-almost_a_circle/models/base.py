#!/usr/bin/python3
""" Defines class Base """
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a Python list object

        Args:
            json_string (str): JSON string of a list of dictionaries
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """
        Retutns an instance with all attributes set

        Args:
            dictionary (dict): A dictionary with key/value attr. pairs
        """
        if dictionary:
            if cls.__name__ == 'Rectangle':
                dummy_instance = cls(1, 1, 0, 0, None)
            elif cls.__name__ == 'Square':
                dummy_instance = cls(1, 0, 0, None)

            dummy_instance.update(**dictionary)
            return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances from json file """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf=8') as f:
                dicts_list = Base.from_json_string(f.read())
                return [cls.create(**dct) for dct in dicts_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes a list of objects to .csv """
        filename = cls.__name__ + '.csv'

        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            if list_objs:
                if cls.__name__ == 'Rectangle':
                    keys = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    keys = ['id', 'size', 'x', 'y']
                writer_obj = csv.DictWriter(csv_file, fieldnames=keys)
                for obj in list_objs:
                    writer_obj.writerow(obj.to_dictionary())
            else:
                csv_file.write('[]')

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes from .csv """
        filename = cls.__name__ + '.csv'

        try:
            with open(filename, 'r', encoding='utf-8') as csv_file:
                if cls.__name__ == 'Rectangle':
                    keys = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    keys = ['id', 'size', 'x', 'y']
                reader_obj = csv.DictReader(csv_file, fieldnames=keys)
                dicts_lst = []
                for dct in reader_obj:
                    for key, value in dct.items():
                        dct[key] = int(value)  # convert value to int
                    dicts_lst.append(dct)
                return [cls.create(**dictionary) for dictionary in dicts_lst]
        except FileNotFoundError:
            return []
