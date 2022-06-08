#!/usr/bin/python3
""" Square Object """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ str model """
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ setter of size """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ setting arguments """
        if args and args is not None:
            for idx in enumerate(args):
                if idx == 0:
                    self.id = args[idx]
                if idx == 1:
                    self.size = args[idx]
                if idx == 2:
                    self.x = args[idx]
                if idx == 3:
                    self.y = args[idx]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Scuaret dictionary """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
