#!/usr/bin/env/python

"""
    manage_columns_filter.py -- add needed columns, remove unused columns
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2016 (c) Michael Conlon"
__license__ = "New BSD License"
__version__ = "0.01"

import sys

from pump.vivopump import read_csv_fp, write_csv_fp, improve_course_title

data_in = read_csv_fp(sys.stdin)
var_names = list(data_in[list(data_in.keys())[1]].keys())  # create a list of var_names from the first row
print("Columns in", var_names, file=sys.stderr)
data_out = {}
for row, data in list(data_in.items()):
    new_data =dict(data)

    # Add these columns

    new_data['remove'] = ''
    new_data['uri'] = ''
    new_data['title'] = improve_course_title(new_data['UF_COURSE_TITLE'])
    new_data['ccn'] = new_data['UF_COURSE_CD']

    # Delete all the upper case column names

    for name in list(new_data.keys()):
        if name == name.upper():
            del new_data[name]

    data_out[row] = new_data
var_names = list(data_out[list(data_out.keys())[1]].keys())  # create a list of var_names from the first row
print("Columns out", var_names, file=sys.stderr)
write_csv_fp(sys.stdout, data_out)





