#!/usr/bin/python3

from models.rectangle import Rectangle

""" Square Class Module"""


class Square(Rectangle):
    """
        This square class inherits from the Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing the Square """
        super().valid_input("size", size, "dime")
        super().valid_input("x", x)
        super().valid_input("y", y)
        super().__init__(size, size, x, y, id)

    # Getter and setter methods for size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        super().valid_input("width", value, "dime")
        self.width = value
        self.height = value

    def __str__(self):
        """ Prints the class string represenation"""
        clsname = type(self).__name__
        _id = self.id
        _x = self.x
        _y = self.y
        s = self.width
        return "[{}] ({}) {}/{} - {}".format(clsname, _id, _x, _y, s)

    def update(self, *args, **kwargs):
        """ update() - assigns arguments to @ attr"""
        if not args:
            if kwargs:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                    elif key == 'size':
                        self.width = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
        else:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id, self.width = args
            elif len(args) == 3:
                self.id, self.width, self.x = args
            elif len(args) == 4:
                self.id, self.width, self.x, self.y = args
        return "[{}] {} {}/{} - {}".format(type(self).__name__, self.id,
                                           self.x, self.y, self.width)

    def to_dictionary(self):
        """ Updating it to square format"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y':
                self.y}
