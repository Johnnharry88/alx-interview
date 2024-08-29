#!/usr/bin/python3
"""Module that makes change using fewest possible coins"""

from math import trunc


def makeChange(coins, total):
    """ Function that determines the fewest number of coins
    needed to make a total chane number"""
    if total < 1:
        return 0
    coins.sort(reverse=True)
    chng = {}
    while total is not None:
        for c in coins:
            if total % c == 0:
                chng[c] = total / c
                return(int(sum(chng.values())))
            else:
                chng[c] = trunc(total / float(c))
                total = total - (c * chng[c])
        return -1
