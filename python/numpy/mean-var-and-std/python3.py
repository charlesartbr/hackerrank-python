import numpy
N,M = map(int,input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(A.mean(axis=1))
print(A.var(axis=0))
print(numpy.round(A.std(), decimals=11))
