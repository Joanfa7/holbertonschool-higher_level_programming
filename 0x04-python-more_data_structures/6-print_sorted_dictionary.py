#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictionary = a_dictionary.items()
    for key, value in sorted(dictionary):
        print("{}: {}".format(key, value))
