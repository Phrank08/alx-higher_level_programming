#!/usr/bin/python3
"""
A module to write an empty class
"""



class BaseGeometry:
    """Geometry class
    """
    def area(self, width, height):
        """
        check area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))





class Rectangle(BaseGeometry):
    """
    A child class that inherits from a parent class
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

