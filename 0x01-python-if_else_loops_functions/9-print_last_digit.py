#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last = number % 10  # Get the last digit of a positive number
    else:
        last = (number * -1) % 10  # Get the last digit of a negative number (by making it positive first)
    print("{:d}".format(last), end="")  # Print the last digit
    return last  # Return the last digit


