#!/usr/bin/python3
""" Function that creates an Oject form a JSONfile """


import json


def load_from_json_file(filename):
    """ creates an object from a JSONfile """
    with open(filename) as f:
       return json.load(f)
