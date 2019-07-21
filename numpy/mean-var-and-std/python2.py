import numpy

n, m = map(int, raw_input().split())

arr = []

for _ in xrange(n):
    arr.append(map(int, raw_input().split()))

my_array = numpy.array(arr)

# to fix the ouput format
numpy.set_printoptions(legacy='1.13')

print numpy.mean(my_array, axis = 1)

print numpy.var(my_array, axis = 0)

print numpy.std(my_array)