#!/usr/bin/python3
""" Reading a file and printig info"""


def read_file(filename=""):
    """ Using the utf-0 mode to open a file and print info"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
