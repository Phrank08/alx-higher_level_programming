#!/usr/bin/python3

def magic_calculation(a, b):
    """Write Python function to match Holberton School provided bytecode."""
    result = 0
    operations = ('add', 'sub')

    from magic_calculation_102 import add, sub

    add_func = add
    sub_func = sub

    if a < b:
        result = add_func(a, b)

        for i in range(4, 6):
            result = add_func(result, i)

    else:
        result = sub_func(a, b)

    return result

