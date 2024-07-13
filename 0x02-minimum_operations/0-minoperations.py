#!/usr/bin/python3
"""method that calculates the fewest number of operations"""


def minOperations(n):
    """
    method that calculates the fewest number of operations
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
