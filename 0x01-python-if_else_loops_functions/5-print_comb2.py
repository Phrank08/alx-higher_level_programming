#!/usr/bin/python3
for y in range(10):
    for x in range(10):
        print("{:d}{:d}".format(y,x), end=', ')
        if y == 9 and x == 9:
            print("{:d}{:d}".format(y,x), end='')
