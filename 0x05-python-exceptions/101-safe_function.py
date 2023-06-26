#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function with provided arguments in a safe manner, catching any exceptions.

    Args:
        fct (function): The function to execute.
        *args: Variable number of arguments to pass to the function.

    Returns:
        The result of the function execution if successful, None otherwise.
    """
    try:
        result = fct(*args)
    except Exception as ex:

        print("Exception: {ex}".format(ex=ex), file=sys.stderr)
        
        return None

    return result
