#!/usr/bin/python3
/* make change */


def calc_total(coins, total):
    if total == 0:
        return 0
    if total < 0:
        return -1

    min_coins = float('inf')
    for coin in coins:
        result = calc_total(coins, total - coin)
        if result != -1:
            min_coins = min(min_coins, result + 1)

    return min_coins if min_coins != float('inf') else -1

def makeChange(coins, total):
    if total < 0:
        return -1
    return calc_total(coins, total)
