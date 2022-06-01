#!/usr/bin/python3
""" funccion that appends a new text to a file """


def append_write(filename="", text=""):
    """ opwn a file, append method, using utf-8
        write a text and return the len of the text appended"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
