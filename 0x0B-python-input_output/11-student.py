#!/usr/bin/python3
""" Defines class Student """


class Student:
    """ class Student """
    def __init__(self, first_name, last_name, age):
        """ Iniialize a new Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """" Retrieve __dict__ of Student instance """
        if isinstance(attrs, list) and\
                (isinstance(attrs[i], str) for i in attrs):
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replace attributes of instance Student """
        for key, value in json.items():
            setattr(self, key, value)
