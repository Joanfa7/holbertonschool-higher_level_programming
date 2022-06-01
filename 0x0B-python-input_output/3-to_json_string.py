#!/usr/bin/python3
""" return json reperesntation of an object"""


import json


def to_json_string(my_obj):
    """ returs a list of objects """
    return json.dumps(my_obj)
