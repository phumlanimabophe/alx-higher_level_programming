#!/usr/bin/python3
""" 0x0A. 0-lookup """


def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    This function takes an object of any type as input and returns a list of its available attributes and methods.

    Args:
        obj (any): The object for which to retrieve the attributes and methods.

    Returns:
        A list of available attributes and methods of the object.
    """

    return dir(obj)
