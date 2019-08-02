#!/bin/python

import math
import os
import random
import re
import sys
import datetime as date

# Complete the time_delta function below.
def time_delta(t1, t2):

    d1 = date.datetime.strptime(t1[4:24], '%d %b %Y %H:%M:%S')
    d2 = date.datetime.strptime(t2[4:24], '%d %b %Y %H:%M:%S')

    h1 = date.timedelta(hours=int(t1[26:28]), minutes=int(t1[28:]))
    h2 = date.timedelta(hours=int(t2[26:28]), minutes=int(t2[28:]))

    if t1[25] == '-':
        d1 += h1
    else:
        d1 -= h1
    
    if t2[25] == '-':
        d2 += h2
    else:
        d2 -= h2

    d = d1 - d2

    return str(int(abs(d.total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):

        t1 = raw_input()
        t2 = raw_input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
