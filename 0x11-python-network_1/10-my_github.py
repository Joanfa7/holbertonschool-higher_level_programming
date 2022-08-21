#!/usr/bin/python3
"""Fetch an URL data """

from sys import argv
from requests.auth import HTTPBasicAuth
import requests


if __name__ == "__main__":
    url = "http://api.github/user"
    r = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    rint(r.json().get('id'))
