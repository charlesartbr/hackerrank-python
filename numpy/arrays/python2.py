import numpy

def arrays(arr):
    npArr = numpy.array(arr, float)
    return npArr[::-1]

arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)