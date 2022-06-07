#!/usr/bin/python3
""" Rectablges class that inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    @property
    def width(self):
        """ width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")


    @property
    def height(self):
        """ height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")


    @property
    def x(self):
        """ x property """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value



    @property
    def y(self):
        """ y property """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """ area of a rectangle h*w """
        return self.__width * self.__height

    def display(self):
        """ Display the rectangle """
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end='')
            for col in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """ method """
        string = "[Rectangle] ({}) {}/{} - {}/{}"
        return string.format(self.id, self.__x, self.__y, self.__width, self.__height)
