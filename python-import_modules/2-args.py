#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_args = len(sys.argv) - 1 #punto llama a funcion
if num_args == 0:
    print("0 arguments.")
elif num_args== 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num_args))
for i in range(1, num_args + 1):
    print("{}: {}".format(i, sys.argv[i]))
