#!/usr/bin/python3
for y in range(9):
    for x in range(10):
        print("{:d}{:d}".format(y, x), end=', ')
        if y == 8 and x == 9:
            print("{:d}{:d}".format(y, x), end='')
