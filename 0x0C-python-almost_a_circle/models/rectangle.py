#!/usr/bin/python3
""" Rectablges class that inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

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
            raise ValueError("x must be >= 0")
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
            raise ValueError("y must be >= 0")
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
        return string.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ setting arguments """
        for idx in range(len(args)):
            if idx == 0:
                self.id = args[idx]
            if idx == 1:
                self.width = args[idx]
            elif idx == 2:
                self.height = args[idx]
            elif idx == 3:
                self.x = args[idx]
            elif idx == 4:
                self.y = args[idx]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
