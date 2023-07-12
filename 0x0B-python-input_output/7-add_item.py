#!/usr/bin/python3
"""Load, add, save  """


from sys import argv
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

argv_edit = argv[1:]

def add_to_json_file(filename, *args):
    """Loads existing data from a JSON file, appends new arguments, and saves the updated data back to the file.

    Args:
        filename (str): Name of the JSON file to be loaded and updated.
        args (tuple): Arguments to be added to the JSON file.

    """
    try:
        content_list = load_from_json_file(filename)
    except FileNotFoundError:
        content_list = []
    content_list.extend(args)
    save_to_json_file(content_list, filename)

if __name__ == '__main__':
    argv_edit = sys.argv[1:]
    add_to_json_file("add_item.json", *argv_edit)