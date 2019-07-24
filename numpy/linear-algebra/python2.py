import numpy

n = int(raw_input())

arr = []

for _ in xrange(n):
    arr.append(map(float, raw_input().split()))

# to fix the ouput format
numpy.set_printoptions(legacy='1.13')

print numpy.linalg.det(arr)