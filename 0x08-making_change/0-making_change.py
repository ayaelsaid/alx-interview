#!/usr/bin/python3


def makeChange(coins, total):
    if total <= 0:
        return 0
    
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if amount >= coin:
                res = amount - coin
                min_coins[amount] = min(min_coins[res] + 1, min_coins[amount])

    return min_coins[total] if min_coins[total] != float('inf') else -1
