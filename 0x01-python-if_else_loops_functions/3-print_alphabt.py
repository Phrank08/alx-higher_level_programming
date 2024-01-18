#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if i == chr('q') or i == chr('e'):
        continue
    print("{}".format(chr(i)), end='')
