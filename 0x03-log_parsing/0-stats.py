#!/usr/bin/python3
""" A module that reads stdin line by line and computes metrics"""

import sys
if __name__ == "__main__":
    # holds count of all status code in a dictionary
    status_code = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                   '404': 0, '405': 0, '500': 0}
    # status_code iterator
    stat = {k: 0 for k in status_code}
    # FIles Size tracker
    size_t = 0
    # keeps record of the number of line
    rec = 0

    # function to print
    def print_out(stat: dict, size_t: int) -> None:
        print('File size: {:d}'.format(size_t))
        for x, y in sorted(stat.items()):
            if y != 0:
                print("{}: {}".format(x, y))
    try:
        for xl in sys.stdin:
            first_line = xl.split()
            rec = rec + 1
            try:
                status_c = first_line[-2]
                if status_c in stat:
                    stat[status_c] += 1
            except BaseException:
                pass
            try:
                file_x = int(first_line[-1])
                size_t = size_t + file_x
            except BaseException:
                pass
            if rec == 10:
                rec = 0
                print_out(stat, size_t)
        print_out(stat, size_t)
    except KeyboardInterrupt:
        print_out(stat, size_t)
        raise
