#!/usr/bin/python3
import sys 
if __name__ == "__main__":     
    sum_of_args = 0
for arg in range(len(sys.argv) -1):
    sum_of_args += int(sys.argv[arg + 1])
print("{}".format(sum_of_args))
