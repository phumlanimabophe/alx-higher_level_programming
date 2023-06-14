#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create an empty matrix to store the squared values
    new_matrix = []

    # Iterate over each row in the input matrix
    for r in matrix:
        # Create a new row to store the squared values of the current row
        squared_row = []

        # Iterate over each element in the current row and square it using map
        for element in r:
            squared_value = element ** 2
            squared_row.append(squared_value)

        # Append the squared row to the new_matrix
        new_matrix.append(squared_row)

    # Return the resulting matrix with squared values
    return new_matrix
