#!/usr/bin/python3
""" Creates an empty class"""


class BaseGeometry:
    """ BaseGeometry class"""

    def area(self):
        """ if the area is not implemente raise an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ check if the data type is an integer """
        if type(value) is not int:
            raise TypeError(f"{name} nust be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
