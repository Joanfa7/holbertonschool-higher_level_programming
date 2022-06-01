#!/usr/bin/python3
""" Module square sub class """


rectangle = __import__('9-rectangle').Rectangle


class Square(rectangle):
    """ Squate subclass """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
