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


