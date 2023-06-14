#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is not empty
    if a_dictionary:
        # Find the key with the highest value using the max function and dictionary's get method as the key parameter
        best_key = max(a_dictionary, key=a_dictionary.get)
        
        # Return the key with the highest value
        return best_key
