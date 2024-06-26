#!/usr/bin/python3
""" A module that estimats the pascals triangel of any number"""


def pascal_triangle(n):
    """returns list of Pascal triangle solution"""
    pasc_sol = []

    # checks for integers qualification
    if n <= 0:
        return triangle
    for x in range(n):
        tri_list = []
        for y in range(x+1):
            if y == 0 or y == x:
                tri_list.append(1)
            else:
                tri_list.append(pasc_sol[x-1][y-1] + pasc_sol[x-1][y])
        pasc_sol.append(tri_list)
    # Display Triangle
    return pasc_sol
