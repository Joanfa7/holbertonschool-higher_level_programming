#!/usr/bin/python3
def text_indentation(text):
    """
    Program tha print a text with 2 new lines after each of '.', '?', ':'

    """
    chars = [".", "?", ":"]

    if type(text) not in [str]:
        raise TypeError("text must be a string")

    for idx in text:
        if idx == ".":
            print(".")
            print( )
        elif idx == "?":
            print("?")
            print( )
        elif idx == ":":
            print(":")
            print( )
        else:
            print(idx, end='')
