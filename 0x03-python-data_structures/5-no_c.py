#!/usr/bin/python3
def no_c(my_string):
    notString = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            notString = notString + char
    return notString
