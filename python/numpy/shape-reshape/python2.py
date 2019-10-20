import numpy

arr = map(int, raw_input().split())

change_array = numpy.array(arr)
change_array.shape = (3, 3)

print change_array  