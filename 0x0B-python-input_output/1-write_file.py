#!/usr/bin/python3

"""
    A module that returns number of characters written

"""

def write_file(filename="", text=""):
    """
    A function that writes a string to a text file
    """

    with open(filename, "w", encoding='UTF-8') as myFile:
        NumCharacters = f.write(text)

        return NumCharacters

