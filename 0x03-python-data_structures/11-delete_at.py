#!/usr/bin/python3
"""a function that deletes the item at a specific position in a list."""
def delete_at(my_list=[], idx=0):
    NewIndex = my_list[idx]
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        del NewIndex
        return NewIndex
