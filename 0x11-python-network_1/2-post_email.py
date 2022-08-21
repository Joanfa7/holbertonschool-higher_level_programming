#!/usr/bin/python3
"""  displays the value of the X-Request-Id """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    email = {'email': sys.argv[2]}

    string = urllib.parse.urlencode(email)
    data = string.encode('ascii')

    with urllib.request.urlopen(sys.argv[1], data) as resp:
        respo_text = resp.read()
        print(respo_text.decode('utf8'))
