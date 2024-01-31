#!/usr/bin/python3


def magic_calculation(a, b):
    """Write Python function to match Holberton School provided bytecode."""
    from magic_calculation_102 import add, sub

    if a < b:
        operations = add(a, b)
        for i in range(4, 6):
            operations = add(operations, i)
        return (operations)

    else:
        return(sub(a, b))
