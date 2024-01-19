#!/usr/bin/python3
for y in range(9):
    for x in range(y+1, 10):
        if y == 8 and x == 9:
            print("{:d}{:d}".format(y, x), end='')
        else:
            print("{:d}{:d}".format(y, x), end=', ')
            print(" ")
