#!/usr/bin/python3
""" check if an object is an instance of a clsas that inherited from 
    the specified class"""


def inherits_from(obj, a_class):
    """ Check the subclass of an object """
    return(issubclass(type(obj), a_class), type(obj) != a_class)
