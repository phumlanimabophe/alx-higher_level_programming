#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Function to raise a NameError exception with a custom message.

    Args:
        message (str): Optional. The custom message to include in the exception. Defaults to an empty string.

    Raises:
        NameError: Exception raised with the provided message.
    """
    raise NameError(message)
