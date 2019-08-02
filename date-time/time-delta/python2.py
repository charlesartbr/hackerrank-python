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

    s1 = (int(t1[26:28]) * 60 * 60) + (int(t1[29]) * 60)
    s2 = (int(t2[26:28]) * 60 * 60) + (int(t2[29]) * 60)
    
    return str(h1) + ' x ' + str(h2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        t1 = raw_input()

        t2 = raw_input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
