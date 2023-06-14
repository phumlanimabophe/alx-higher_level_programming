#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Create a new set to store the common elements
    new_set = {x for x in set_1 if x in set_2}
    
    # Return the new set containing the common elements
    return new_set
