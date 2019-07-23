import numpy

n, m = map(int, raw_input().split())

arr = []

for _ in xrange(n):
    arr.append(map(int, raw_input().split()))

narr = numpy.array(arr)

print narr.transpose()
print narr.flatten()
