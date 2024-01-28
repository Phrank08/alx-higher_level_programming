#!/usr/bin/python3

if __name__ == "__main__":
    """prints all the  functions from calculator_1 and handles basic operations."""

    from calculator_1 import *
    import sys

    if len(sys.srgv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        a = int(sys.argv[1])
        operator = (sys.argv[2])
        b = int(sys.argv[3])

        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a / b
        else:
            print("Unknown operator. Available operators: +, -, * and /")
