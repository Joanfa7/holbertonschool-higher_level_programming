#!/usr/bin/python3
"""Fetch an URL data """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as respo:
        data = respo.read()
        print("Body response:")
        print("    - type: {}".format(type(data)))
        print("    - content: {}".format(type(data)))
        print("    - utf8 content: {}".format(type(data.decode("UTF-8"))))

