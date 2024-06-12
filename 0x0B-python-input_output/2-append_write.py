#!/usr/bin/python3

"""
A module that appends to a file
"""


def append_write(filename="", text=""):
    """
    A function that appends to a file and 
    returns number of characters
    """

    with open(filename, 'a', encoding='UTF-8') as myFile:
        NumCharacters = myFile.write(text)
        return NumCharacters
