#!/usr/bin/python3
""" Module that writes an Object to a text file """


import json


def save_to_json_file(my_obj, filename):
    """ save object to a JSON file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
