#!/usr/bin/python3
"""Defines playing a game with primes."""


def find_prime(n):
    """
    Find the prime numbers up to n.
    Args:
        n (int): The upper limit to find primes (inclusive).
    Returns:
        list: A list of prime numbers from 2 to n (inclusive).
    """
    if n < 2:
        return [] 
    primes = [True] * n
    primes[0] = False

    p = 2
    while p * p <= n:
        if primes[p - 1]:
            for i in range(p * p, n + 1, p):
                primes[i - 1] = False
        p += 1
    all_primes = [i for i in range(2, n + 1) if primes[i - 1]]
    return all_primes


def isWinner(x, nums):
    """
    Determine the winner of the prime game between Maria and Ben.
    Args:
        x (int): The number of rounds.
        nums (list of int): List of numbers to check for each round.
    Returns:
        str: The name of the player who won the most rounds ("Maria" or "Ben").
             If it's a tie, return "None".
    """
    ben = 0
    maria = 0

    if x < 10000:
        for i in range(x):
            n = nums[i]
            if n < 2:
                ben += 1
                continue
            if n < 10000:
                primes = find_prime(n)
                used_primes = len(primes)
                if used_primes % 2 == 0:
                    ben += 1
                else:
                    maria += 1
    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None
