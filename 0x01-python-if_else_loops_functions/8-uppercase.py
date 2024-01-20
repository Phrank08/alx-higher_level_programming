#!/usr/bin/python3
def uppercase(str):
    for char in str:
        alpha_num = ord(char)
        if 97 <= alpha_num <= 122:
            alpha_num -= 32
            print("{}".format(chr(alpha_num)), end='')
        else:
            print("{}".format(chr(alpha_num)), end='')
        print("")
