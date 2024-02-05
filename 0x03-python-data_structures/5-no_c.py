#!/usr/bin/python3
"""a function that removes all characters c and C from a string."""
def no_c(my_string):
    notString = ''
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            notString += ch
            return notString
