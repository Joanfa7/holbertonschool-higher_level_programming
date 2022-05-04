#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictionary = a_dictionary.items()
    for i, j in sorted(dictionary):
        print(i, ":", j)
