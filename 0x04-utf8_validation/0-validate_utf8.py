#!/usr/bin/python3
"""A method that checks an input data to validate its
utf8 encoding"""


def validUTF8(data):
    """Function that validates utf8 data
    Returns True if utf8 else false"""
    trak = 0
    s = len(data)
    for x in range(len(data)):
        if trak > 0:
            trak = trak - 1
            continue
        if type(data[x]) != int or data[x] < 0 or data[x] > 0x10ffff:
            return False
        elif data[x] <= 0x7f:
            trak = 0
        elif data[x] & 0b11111000 == 0b11110000:
            space = 4
            if s - x >= space:
                n_body = list(map(
                    lambda n: n & 0b11000000 == 0b10000000,
                    data[n + 1: n + space],
                ))
                if not all(n_body):
                    return False
                trak = space - 1
            else:
                return False
        elif data[x] & 0b11110000 == 0b11100000:
            space = 3
            if s - x >= space:
                n_body = list(map(
                    lambda n: n & 0b11000000 == 0b10000000,
                    data[x + 1: x + space],
                ))
                if not all(n_body):
                    return False
                trak = space - 1
            else:
                return False
        elif data[x] & 0b11100000 == 0b11000000:
            space = 2
            if s - x >= space:
                n_body = list(map(
                    lambda n: n & 0b11000000 == 0b10000000,
                    data[x + 1: x + space],
                ))
                if not all(n_body):
                    return False
                trak = space - 1
            else:
                return False
        else:
            return False
    return True
