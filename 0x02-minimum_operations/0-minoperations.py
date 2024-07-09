#!/usr/bin/python3
""" Minimum operation coding challenge"""


def minOperations(n):
    """Computes the fewest no of operaions
    in exactly in H characters.
    """
    if not isinstance(n, int):
        return 0
    count_ops = 0
    clipper = 0
    complete = 1

    while complete < n:
        if clipper == 0:
            clipper = complete
            complete = complete + clipper
            count_ops = count_ops + 2

        elif n - complete > 0 and (n - complete) % complete == 0:
            clipper = complete
            complete = complete + clipper
            count_ops = count_ops + 2

        elif clipper > 0:
            complete = complete + clipper
            count_ops = count_ops + 1
    return count_ops
