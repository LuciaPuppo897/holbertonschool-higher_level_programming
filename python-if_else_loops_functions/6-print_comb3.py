#!/usr/bin/python3
for num in range(0, 10):
    for num2 in range(num + 1, 10):
        if num != 8:
            print("{}{}, ".format(num, num2), end='')
        else:
            print("{}{}".format(num, num2))
