#!/usr/bin/python3
"""This is a class square"""


class Square:
    """Definnig the private instance size"""
    def __init__(self, size=0):
        self.__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        area = self.__size ** 2
        return(area)

