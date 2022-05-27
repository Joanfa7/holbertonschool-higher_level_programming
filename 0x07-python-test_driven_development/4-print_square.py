#!/usr/bin/python3
def print_square(size):
    """
    program the print a square


    """

    try:
        for col in range(size):
            for row in range(size):
                print("#", end="")
            print()

    except:
        if type(size) not in [int]:
            raise TypeError("size must be an integer")
    else:
        if size < 0:
            raise ValueError("size must be >= 0")

