#!/usr/bin/python3
"""a function that finds all multiples of 2 in a list."""
def divisible_by_2(my_list=[]):
    if my_list is not None:
        i = 0
        NewString = []
        for element in my_list:
            if my_list[i] % 2 == 0:
               NewString.append(True)
           else:
               NewString.append(False)
            i += 1
        return NewString
