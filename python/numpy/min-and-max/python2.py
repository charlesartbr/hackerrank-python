import numpy

n, m = map(int, raw_input().split())

arr = []

for _ in xrange(n):
    arr.append(map(int, raw_input().split()))

my_array = numpy.array(arr)

min = numpy.min(my_array, axis = 1)

print numpy.max(min)