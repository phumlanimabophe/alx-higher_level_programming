#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create an empty list to store the modified values
    new_list = []

    # Iterate over each element in the input list
    for num in my_list:
        # Check if the current element matches the search value
        if num == search:
            # If there's a match, append the replace value to the new_list
            new_list.append(replace)
        else:
            # If no match, append the current element as is to the new_list
            new_list.append(num)

    # Return the modified list with replacements
    return new_list
