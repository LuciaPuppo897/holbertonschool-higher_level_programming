#!/usr/bin/python3
from sys import argv
args = argv[1:]
sum_of_args = 0

for arg in args:
    sum_of_args += int(arg)
print("{}".format(sum_of_args))
