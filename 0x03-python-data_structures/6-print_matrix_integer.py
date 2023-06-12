#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        # Iterate over each element in the current row
        for j in range(len(matrix[i])):
            # Check if it's the last element in the row
            if j < len(matrix[i]) - 1:
                # Print the element with a space at the end
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                # Print the last element without a space at the end
                print("{:d}".format(matrix[i][j]), end="")

        # Move to the next line after printing each row
        print("")