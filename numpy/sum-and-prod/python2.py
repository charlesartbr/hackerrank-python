import numpy

n, m = map(int, raw_input().split())

arr = []

for _ in xrange(n):
    arr.append(map(int, raw_input().split()))

my_array = numpy.array(arr)

sum = numpy.sum(my_array, axis = 0)

print numpy.prod(sum, axis = 0)