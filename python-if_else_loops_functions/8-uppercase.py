#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char = ord(char)
        if char >= ord('a') and char <= ord('z'):
            char -= 32
        print("{}".format(chr(char)), end='')
    print()
