#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("\n" if col == row[-1] else "{:d}".format(col), end=" ")
