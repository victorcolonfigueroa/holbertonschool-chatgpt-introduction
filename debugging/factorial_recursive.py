#!/usr/bin/python3
"""Calculate factorial of a number provided as a command-line argument."""

import sys


def factorial(n):
    """Calculate factorial of a non-negative integer.

    Args:
        n (int): The number whose factorial is to be calculated.

    Returns:
        int: The factorial of the input number.
    """
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
