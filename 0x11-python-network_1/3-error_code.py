#!/usr/bin/python3
"""  displays the value of the X-Request-Id """
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('utf8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
