#!/bin/python3

import os
from datetime import datetime, timedelta

# Complete the time_delta function below.
def time_delta(t1, t2):

    d1 = datetime.strptime(t1[4:24], '%d %b %Y %H:%M:%S')
    d2 = datetime.strptime(t2[4:24], '%d %b %Y %H:%M:%S')

    h1 = timedelta(hours=int(t1[26:28]), minutes=int(t1[28:]))
    h2 = timedelta(hours=int(t2[26:28]), minutes=int(t2[28:]))

    d1 = d1 + h1 if t1[25] == '-' else d1 - h1
    d2 = d2 + h2 if t2[25] == '-' else d2 - h2

    return str(int(abs((d1 - d2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):

        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
