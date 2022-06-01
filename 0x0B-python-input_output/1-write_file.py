#!/usr/bin/python3
""" Writes a text in a file using utf-8 """


def write_file(filename="", text=""):
    """ open a file, write given text and return the len of text """
    with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(text)
            return len(text)
