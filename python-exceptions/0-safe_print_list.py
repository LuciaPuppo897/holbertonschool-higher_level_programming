#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0  
        for i in range(x):
            print(my_list[i], end=" ")
            count += 1
        return count
    except IndexError: # Handle when index is out of range
        pass
        print()
        return count
