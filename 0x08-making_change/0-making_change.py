#!/usr/bin/python3
"""
0-making_change module
"""


def makeChange(coins, total):
    """
        A function that find min number to reach target amount.
    """
    if total < 1:
        return 0
    number = 0
    prev_total = total
    coins = sorted(coins, reverse=True)
    while total > 0:
        prev_total = total
        for coin in coins:
            if (total - coin) >= 0:
                total -= coin
                number += 1
                break
        if total == prev_total:
            break
    if number == 0 or total != 0:
        return -1
    return number
