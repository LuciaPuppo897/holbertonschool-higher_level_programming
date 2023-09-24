#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1

if num_args == 0:
    print("Number of arguments: 0.")
    print(".")
else:
    args_text = "arguments" if num_args > 1 else "argument"
    print("Number of {}: {}.".format(args_text, num_args))

    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))
