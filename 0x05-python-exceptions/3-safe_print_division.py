#!/usr/bin/python3
def safe_print_division(a, b):
    outcome = none
    try:
        outcome = a / b
except ZeroDivisionError:
    return outcome
finally:
    print("Inside outcome: {}".format(outcome))
    return outcome
