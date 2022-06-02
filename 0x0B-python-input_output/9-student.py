#!/usr/bin/python3
""" Module of an class object """


class Student:
    """ Defining student class """

    def __init__(self, first_name, last_name, age):
        """ student public atributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ a json object """
        return self.__dict__
