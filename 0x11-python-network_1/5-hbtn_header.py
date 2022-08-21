#!/usr/bin/python3
"""Fetch an URL data """

from sys import argv
import requests


if __name__ == "__main__":
    reque = requests.get('argv[1]')
    print(reque.headers.get('X-Request-Id'))
