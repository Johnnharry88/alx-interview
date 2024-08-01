#!/usr/bin/python3
"""Module that finds solutions for nqueen"""
import sys

# list of possible solutions
sol = []
# size of cheese board n
n = 0
# possibe positions of quenn on chessboard
pos = None


def input_getter():
    """Checks program inputs and validates ;t """
    global n 
    n  = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    else:
        try:
            n = int(sys.argv[1])
        except Exception:
            print("N must be a numbre")
            sys.exit(1)
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        return n


def attacking_queen(pos0, pos1):
    """Checks for that attacking mode of two queens"""
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def existing_grp(group):
    """Checks out a group in the solution list"""
    global sol
    for s in sol:
        x = 0
        for s_pos in s:
            for g_pos in group:
                if s_pos[0] == g_pos[0] and s_pos[1] == g_pos[1]:
                    x += 1
        if x == n:
            return True
    return False

def solver(row, group):
    """Solution for hte nqueens problem"""
    global sol
    global n
    if row == n:
        top0 = group.copy()
        if not existing_grp(top0):
            sol.append(top0)
    else:
        for c in range(n):
            x = (row * n) + c
            check = zip(list([pos[x]]) * len(group), group)
            used_pos = map(lambda n: attacking_queen(n[0], n[1]), check)
            group.append(pos[x].copy())
            if not any(used_pos):
                solver(row + 1, group)
            group.pop(len(group) - 1)


def get_sol():
    """Retrieves solution for given chessboard size"""
    global pos, n
    pos = list(map(lambda x: [x //n, x% n], range(n ** 2)))
    a = 0
    group = []
    solver(a, group)


n = input_getter()
get_sol()
for s in sol:
    print(sol)
