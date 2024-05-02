#!/usr/bin/python3

"""
A function that returns a boolean value
"""

def is_same_class(obj, a_class):
    """
    a function that checks if the specified object ia an instance of
    the specified class
    """


    if type(obj) == a_class:
        return True
    """
    returns True if Yes
    """

    else:
        return False
    """
    returns False if No 
