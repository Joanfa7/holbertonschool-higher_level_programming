#!/usr/bin/python3
""" Function that returns True if the object is exactly an intance
    of the specified class, other wise False """


def is_same_class(obj, a_class):
    """ Return True if is type or false if not"""
    if type(obj) is a_class:
        return True
    else:
        return False
