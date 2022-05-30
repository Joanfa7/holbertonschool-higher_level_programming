#!/usr/bin/python3
""" check if an object is an instance of a clsas that inherited from 
    the specified class"""


def inherits_from(obj, a_class):
    """ Check the subclass of an object """
    if issubclass(type(obj), a_class):
        return True
    elif type(obj) != a_class:
        return True
    else:
        return False
