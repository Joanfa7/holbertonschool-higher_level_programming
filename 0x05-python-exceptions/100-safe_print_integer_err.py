#!/usr/bin/python3
import sys
__name__ == "__main__"
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        print("Exception:",file = sys.stderr)
        return(False)
    else:
        return(True)

