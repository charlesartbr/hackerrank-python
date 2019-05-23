#!/bin/python3

N = int(input())

if N % 2 == 1:
    print("Weird")
elif N % 2 == 0 and N >= 6 and N <= 20:
    print("Weird")
else:
    print("Not Weird")