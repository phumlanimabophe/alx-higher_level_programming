#!/usr/bin/python3
def read_file(filename):
    """Reads the contents of a text file and prints them to stdout.

    Args:
        filename (str): Name of the file to be opened.

    """
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
    print(contents, end='')

