#!/usr/bin/python3
""" Returns the dictionary descripton with simple
    data structre for JSON serialization of an object """


def class_to_json(obj):
    """ object class """

    
    return obj.__dict__
