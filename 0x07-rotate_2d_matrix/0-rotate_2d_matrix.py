#!/usr/bin/python3
"""Module that rotates matrix"""


def transpose_mat(matrix, n):
    for x in range(n):
        for y in range(x, n):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]


def reverse_matrix(matrix):
    for i in matrix:
        i.reverse()


def rotate_2d_matrix(matrix):
    n = len(matrix)
    transpose_mat(matrix, n)
    reverse_matrix(matrix)
    return matrix
