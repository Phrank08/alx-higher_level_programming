#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division
[2;2R[3;1R[>77;30603;0c]10;rgb:0000/ffff/4040]11;rgb:0000/0000/0000
a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
