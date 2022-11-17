#!/usr/bin/env/python

"""
    privacy_filter.py -- remove ufids with privacy protection, or that can not be found in the privacy data
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2016 (c) Michael Conlon"
__license__ = "New BSD License"
__version__ = "0.01"

import shelve
import sys

from pump.vivopump import read_csv_fp, write_csv_fp

privacy_shelve = shelve.open('privacy.db')
privacy_ufids = set(privacy_shelve.keys())  # a set of ufids that have privacy information
data_in = read_csv_fp(sys.stdin)
print("Privacy start", len(data_in), file=sys.stderr)
okay = 0
protected = 0
not_found = 0
data_out = {}
for row, data in list(data_in.items()):
    if data['UFID'] in privacy_ufids:  # must have privacy information
        if privacy_shelve[data['UFID']]['UF_SECURITY_FLG'] == 'N' and privacy_shelve[data['UFID']][
                'UF_PROTECT_FLG'] == 'N':
            data_out[row] = data
            okay += 1
        else:
            protected += 1
    else:
        not_found +=1
print("Okay", okay, file=sys.stderr)
print("Protected", protected, file=sys.stderr)
print("Not Found", not_found, file=sys.stderr)
print("Privacy End", len(data_out), file=sys.stderr)
write_csv_fp(sys.stdout, data_out)
privacy_shelve.close()





