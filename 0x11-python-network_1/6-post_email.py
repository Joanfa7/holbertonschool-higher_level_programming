#!/usr/bin/python3
"""Fetch an URL data """

from sys import argv
import requests


if __name__ == "__main__":
    email = {"email": argv[2]}
    reque = requests.post(argv[1], email)
    print(reque.text)
