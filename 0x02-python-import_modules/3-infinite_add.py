#!/usr/bin/python3
from math import inf
from sys import argv
if __name__ == "__main__":

    n = len(argv)
    length = len(argv)
    Sum = 0

    for i in range(1, n):
        Sum += int(argv[i])
    print(Sum)
