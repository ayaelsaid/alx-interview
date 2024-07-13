#!/usr/bin/python3
"""Method that calculates the fewest number of operations."""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to reach n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required, or 0 if n is impossible.
    """
    if n <= 0:
        return 0
    factor = 2
    op = 0

    while n > 1:
        while n % factor == 0:
            op += factor
            n //= factor
        
        factor += 1
    return op
