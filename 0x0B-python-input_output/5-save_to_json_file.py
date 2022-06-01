#!/usr/bin/python3
""" Module that writes an Object to a text file """


import json


def save_to_json_file(my_obj, filename):
    """ save object to a JSON file"""
    json_object = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.writelines(json_object)
