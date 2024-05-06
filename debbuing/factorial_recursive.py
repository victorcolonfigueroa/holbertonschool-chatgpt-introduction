#!/usr/bin/python3
import sys

# Define a function to calculate the factorial of a number
def factorial(n):
    # Base case: If n is 0, factorial is 1
    if n == 0:
        return 1
    # Recursive case: Multiply n by the factorial of (n-1)
    else:
        return n * factorial(n-1)

# Get the command-line argument passed to the script and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the factorial result
print(f)

