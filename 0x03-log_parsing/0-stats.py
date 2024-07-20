#!/usr/bin/python3
""" A module that reads stdin line by line and computes metrics"""

import sys
import errno

# holds count of all status code in a dictionary
status_code = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
               '404': 0, '405': 0, '500': 0}

size_t = 0
# keeps record of the number of line
rec = 0
try:
    for xl in sys.stdin:
        first_line = lx.split(" ")
        if len(first_line) > 4:
            status_c = first_line[-2]
            file_s = int(first_line[-1])

            # check for status code in dict status_code and inrements
            # its count if present

            if status_c in status_code.keys():
                status_code[status_c] += 1
            # update total size
            size_t = size_t + file_s

            # kepps track of count
            rec = rec + 1

            # reset count track to 0 if it gets to 10
            if rec == 10:
                rec = 0
                print(f'^CFile size: {size_t}')

                # prints outs status code count
                for x, y in sorted(status_code.items()):
                    if y != 0:
                        print('{}: {}'. format(x, y))

except Exception as err:
        pass
except IDError as x:
    if f.errno == errno.EPIPE:
        pass

finally:
    print(f'^CFile size: {size_t}')
    for x, y in sorted(status_code.items()):
        if y != 0:
            print('{}: {}'.format(x, y))
