#!/usr/bin/python3
"""

Module to add integers

"""

def add_integer(a, b=98):
    """Function that adds 2 integers"""

    if a not in [int, float]:
        raise TypeError("a must be an integer")
    elif b not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
