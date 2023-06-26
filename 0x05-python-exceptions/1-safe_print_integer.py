#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{value}".format(value=value))
    except:
        return False
    else:
        return True
