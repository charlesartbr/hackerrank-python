import numpy

n = int(raw_input())

a = []
b = []

for _ in xrange(n):
    a.append(map(int, raw_input().split()))

for _ in xrange(n):
    b.append(map(int, raw_input().split()))

print numpy.dot(a, b)