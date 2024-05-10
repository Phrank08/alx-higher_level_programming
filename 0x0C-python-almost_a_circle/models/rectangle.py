#!/usr/bin/python3

"""
A class module
"""

class Base:
    """
    A class named named Base
    """
    __nb_objects = 0
    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

class Rectangle(Base):
    """
    A sub class from the super class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        return self.width

    def set_width(self):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self):
        self.height = height

    def get_x(self):
        return self.x

    def set_x(self):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self):
        self.y = y


