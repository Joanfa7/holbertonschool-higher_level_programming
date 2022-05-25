#!/usr/bin/python3
def magic_string(n):
    for i in range(n):
        for j in range(n, i + 1):
            print("#", end="")
    print()
