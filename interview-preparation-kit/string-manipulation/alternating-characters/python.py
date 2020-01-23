#!/bin/python

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    
    n = 0
    last = ''
    
    for c in s:

        if c == last:
            n += 1

        last = c

    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
