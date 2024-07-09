#!/usr/bin/python3
""" a function that returns True if the object is exactly an instance of the s       pecified class ; otherwise False.
"""

def is_same_class(obj, a_class):
    """Check if they are same object"""
    return type(obj) is a_class
