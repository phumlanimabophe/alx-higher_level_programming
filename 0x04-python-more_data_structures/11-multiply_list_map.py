#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # Define a helper function to multiply an element by the given number
    def multiply_element(element):
        return element * number

    # Use the map function with the helper function to multiply each element in the list
    multiplied_list = list(map(multiply_element, my_list))

    # Return the multiplied list
    return multiplied_list
