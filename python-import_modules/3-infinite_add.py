#!/usr/bin/python3
if __name__ == "__main__":
    import sys 
sum_of_args = 0

for arg in range(len(sys.argv)-1):
    sum_of_args += int(arg)
print("{}".format(sum_of_args))
