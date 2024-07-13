#!/usr/bin/python3
"""Method that calculates number of operations."""


def minOperations(n):
    """
    Calculate number of operations needed to reach n
    Args:
        n (int): The target number
    Returns:
        int: The minimum number , or
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
