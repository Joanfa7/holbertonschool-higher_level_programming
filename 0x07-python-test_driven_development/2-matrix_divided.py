#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Function that divides all elemento of a metrix """
    
    length = len(matrix[0])
    new_matrix = list(map(list, matrix))

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a list of list")

    for col in range(len(new_matrix)):
            for row in range(len(new_matrix[col])):
                if type(row) not in [int, float]:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                new_matrix[col][row] = round(new_matrix[col][row]/div, 2)

    return(new_matrix)

