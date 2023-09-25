#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in range(len(matrix)):
        for co in range(len(matrix[r])):
            if co != len(matrix[co]) - 1:
                print("{:d}".format(matrix[r][co], end= ""))
        else:
                print("{:d}".format(matrix[r][co], end= ""))
        print()
