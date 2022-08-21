#!/usr/bin/python3
"""Fetch an URL data """

from sys import argv
import requests


if __name__ == "__main__":
    reque = requests.get(argv[1])
    if reque.status_code >= 400:
        print("Error code: {}".format(reque.status_code))
    else:
        print(reque.text)
