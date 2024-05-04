#!/usr/bin/python3
"""
A module that reads file to the standard output
"""

def read_file(filename=""):
    """A function that reads a text file (UTF8) 
    and prints it to stdout
    """
    with open("filename", encoding "UTF=8") as myFile:
        TextContainer = myFile.read()
        print(TextContainer, end="")

