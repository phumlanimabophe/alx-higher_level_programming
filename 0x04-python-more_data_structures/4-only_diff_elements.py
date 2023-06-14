#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create a list containing two sets: elements in set_1 but not in set_2, and elements in set_2 but not in set_1
    to_use = [{x for x in set_1 if x not in set_2}, {x for x in set_2 if x not in set_1}]
    
    # Combine the two sets using the union operator | to get all unique elements
    # that are present in either set_1 or set_2
    return to_use[0] | to_use[1]
