#!/usr/bin/python3
"""Module holding Solution to lockboxes problem:"""


def canUnlockAll(boxes):
    """Checks if the boxes can be unlocked"""
    if (type(boxes) is not list or len(boxes) == 0):
        return False
    for x in range(1, len(boxes) - 1):
        unlok = False
        for a in range(len(boxes)):
            unlok = x in boxes[a] and x != a
            if unlok:
                break
        if unlok is False:
            return unlok
    return True
