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
        """ setter of size """
        self.width = value
        self.height = value

    def __str__(self):
        """ str model """
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ setting arguments """
        for idx in range(len(args)):
            if idx == 0:
                self.id = args[idx]
            if idx == 1:
                self.size = args[idx]
            if idx == 2:
                self.x = args[idx]
            if idx == 3:
                self.y = args[idx]

        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            if key == 'size':
                self.width = value
            if key == 'x':
                self.x = value
            if key == 'y':
                self.y = value

