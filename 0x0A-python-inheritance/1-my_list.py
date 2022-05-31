#!/usr/bin/python3
""" prints the list, but sorted (ascending sort) """


class MyList(list):
    """ MyList class ineriting from list"""
    def print_sorted(self):
        print(sorted(self))
