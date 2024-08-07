#!/usr/bin/python3
"""This is a module that defines a rectangle"""

class Rectangle:
    """ A class that defines a Rectangle class with diffrent method to set the height and width
    """
    
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        
    @property
    def width(self):
        """Returns the rectangle width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value  
    
    @property
    def height(self):
        """Returns the rectangle Height"""
        return self.__height
    
    @height.setter  
    def height(self, value):
        """Set the height of the rectangle."""
        
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
            
