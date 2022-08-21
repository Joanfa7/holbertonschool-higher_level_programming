#!/usr/bin/python3
"""Fetch an URL data """

from sys import argv
import requests


if __name__ == "__main__":
    try:
        query = {"q": argv[1]}
    except:
        query = {"q": ""}
    url = "http://0.0.0.0:5000/search_user"
    try: 
        r = requests.post(url, query)
        if (r.json().get('id') is not None):
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
