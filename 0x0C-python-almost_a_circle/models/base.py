#!/usr/bin/python3
""" manage id attribute in all classes """


import json


class Base:
    """ Base class object """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictrionaries):
        if not list_dictrionaries or list_dictrionaries is None:
            return "[]"
        return json.dumps(list_dictrionaries)

    @staticmethod
    def from_jason_string(json_string):
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([i.to_dictionary() for i in list_objs]))
