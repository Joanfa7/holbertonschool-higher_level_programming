#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for col in range(len(matrix)):
        new_matrix = [[col*col for col in row] for row in matrix]
    return new_matrix
