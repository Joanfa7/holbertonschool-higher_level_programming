#!/usr/bin/python3


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        string = "[Square] ({}) {}/{} - {}/{}"
        return string.format(self.id, self.x, self.y, self.width, self.height)



