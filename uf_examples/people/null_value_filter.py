#!/usr/bin/env/python

"""
    null_value_filter.py -- Replace "NULL" with empty string
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2016 (c) Michael Conlon"
__license__ = "New BSD License"
__version__ = "0.01"

import sys

from pump.vivopump import read_csv_fp, write_csv_fp

data_in = read_csv_fp(sys.stdin)
data_out = {}
null_count = 0
for row, data in list(data_in.items()):
    new_data =dict(data)
    for name, val in list(new_data.items()):
        if val == "NULL":
            new_data[name] = ""
            null_count += 1
    data_out[row] = new_data
print("NULL values replaced", null_count, file=sys.stderr)
write_csv_fp(sys.stdout, data_out)





