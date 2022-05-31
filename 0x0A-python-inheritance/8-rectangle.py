#!/usr/bin/python3
""" Creates an empty class"""


variable = __import__('7-base_geometry').BaseGeometry


class Rectangle(variable):
    """ Rectablge object inheritate from BaseGeometry """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator(self, "width", width)
        super().integer_validator(self, "height", height)
