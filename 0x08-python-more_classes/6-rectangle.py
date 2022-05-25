#!/usr/bin/python3
""" Define a rectangle class object """


class Rectangle:
    """ Rectangle Object """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        area = (self.__height * self.__width)
        return(area)

    def perimeter(self):
        if self.__height == 0 or self.width == 0:
            perimeter = 0
            return(perimeter)
        perimeter = 2 * (self.__height + self.__width)
        return(perimeter)

    def __str__(self):
        list = []
        separator = ""
        if self.__width == 0 or self.__height == 0:
            return("")
        for i in range(self.__height):
            list.append("#" * self.__width)
            if i != self.__height - 1:
                list.append("\n")
        return separator.join(list)

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
