#!/usr/bin/python3
"""
a class BaseGeometry (based on 6-base_geometry.py).
"""

class BaseGeometry:
    """
    a class named BAseGeometry
    """

    def area(self):
        """
        checks area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        checks for an integer
        """
        self.name = str(name)
        self.value = value

        if value not in int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


