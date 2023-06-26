#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{v}".format(v=value))
    except Exception as e:
        print("Exception: {v}".format(v=e), file=sys.stderr)
        return False
    return True
