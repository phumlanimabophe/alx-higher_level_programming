#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):  # Iterate over numbers from 1 to 100
        if i % 15 == 0:  # Check if the number is divisible by both 3 and 5
            print("FizzBuzz", end=" ")  # Print "FizzBuzz"
        elif i % 3 == 0:  # Check if the number is divisible by 3
            print("Fizz", end=" ")  # Print "Fizz"
        elif i % 5 == 0:  # Check if the number is divisible by 5
            print("Buzz", end=" ")  # Print "Buzz"
        else:
            print("{:d}".format(i), end=" ")  # Print the number itself

# Call the fizzbuzz function when done


