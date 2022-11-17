#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    unique_name_filter.py -- remove duplicate name
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2015 (c) Michael Conlon"
__license__ = "New BSD License"
__version__ = "0.01"

import sys

from pump.vivopump import read_csv_fp, write_csv_fp

data_in = read_csv_fp(sys.stdin)
print("Input rows", len(data_in), file=sys.stderr)

data_out = {}
name_out = set()

for row, data in list(data_in.items()):
    new_data = dict(data)
    if data['name'] not in name_out:
        data_out[row] = new_data
        name_out.add(data['name'])
print("Output rows", len(data_out), file=sys.stderr)
write_csv_fp(sys.stdout, data_out)
