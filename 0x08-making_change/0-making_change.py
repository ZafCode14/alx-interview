#!/usr/bin/python3
"""Module with a python script"""


def makeChange(coins, total):
    """Function that determines the fewest number of coins"""
    if total < 0:
        return 0
    if total == 0:
        return 0
    if not coins:
        return -1

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

