from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1

if num_args == 0:
    print("Number of arguments: 0.")
    print(".")
else:
     print("Number of argument{}: {}.".format('s' if num_args > 1 else '', num_args))

for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))