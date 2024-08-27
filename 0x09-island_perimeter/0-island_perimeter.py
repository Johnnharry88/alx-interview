#!/usr/bin/python3
"""Module that defined island Perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of an island"""
    wid = len(grid[0])
    hgt = len(grid)
    edges = 0
    size = 0

    for x in range(hgt):
        for y in range(wid):
            if grid[x][y] == 1:
                size = size + 1
                if (y > 0 and grid[x][y - 1] == 1):
                    edges = edges + 1
                if (x > 0 and grid[x - 1][y] == 1):
                    edges = edges + 1
    return size * 4 - edges * 2
