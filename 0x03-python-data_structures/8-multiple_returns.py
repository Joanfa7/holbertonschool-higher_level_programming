#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    char1 = sentence[0]
    if sentence == "":
        return [0, None]
    else:
        return [length, char1]
