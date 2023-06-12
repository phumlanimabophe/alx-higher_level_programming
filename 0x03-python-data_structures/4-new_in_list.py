#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    # Check if the index is out of range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Create a copy of the original list
    new_list = my_list[:]

    # Replace the element at the specified index with the new element
    new_list[idx] = element

    # Return the new list
    return new_list
