#!/usr/bin/python3
""" 0x0A. 101-add_attribute """


def add_attribute(obj, attribute, value):
    """
    Attempts to set or update an attribute with a given value in the object.

    Args:
        obj (any): The object to have the attribute set.
        attribute (str): The name of the new/updated attribute.
        value (any): The value to set for the attribute.

    Raises:
        TypeError: If adding or updating the attribute is not possible.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    elif hasattr(obj, "__slots__") and attribute in obj.__slots__:
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
