#!/usr/bin/python3
"""
A class that raises an exception
"""

class BaseGeometry:
    """
    A class named BaseGeometry
    """
    def area(self):
        """
        check area
        """
        raise Exception("area() is not implemented")
