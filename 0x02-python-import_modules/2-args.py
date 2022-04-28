#!/usr/bin/python3
import sys

length = len(sys.argv)-1
ctr = 0

if length == 0:
    print("0 arguments.")

elif length == 1:
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(length))
    for idx in range(1, length + 1):
        ctr += 1
        print("{}: {}".format(ctr, sys.argv[idx]))
