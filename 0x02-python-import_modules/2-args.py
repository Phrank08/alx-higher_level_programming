#!/usr/bin/python3

if __name__ == "__main__":
    """ prints the number of and the list of its arguments."""
    import sys

    char_num = len(sys.argv) - 1
    if char_num == 0:
        print("0 arguments.")
    elif char_num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(char_num))
    for i in range(char_num):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
~                                                           
