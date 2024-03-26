#!/usr/bin/python3
def safe_print_division(a, b):
    result = none
    try:
        result = a / b
except ZeroDivisionError:
    return result
finally:
    print("Inside outcome: {}".format(result))
    return result
