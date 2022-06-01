#!/usr/bin/python3
""" Module that returns an object represented by a
    JSON string """


import json


def from_json_string(my_str):
    """ returns a representation of an object """
    return json.loads(my_str)
