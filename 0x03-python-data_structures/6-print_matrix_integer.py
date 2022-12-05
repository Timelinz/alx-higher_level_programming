#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix in the format
    x x x
    x x x
    x x x
    --
    Args:
        matrix - a matrix of integers default [[]]
    """
    for row in matrix:
        fmt = " ".join(["{:d}" for x in row])
        print(fmt.format(*row))
