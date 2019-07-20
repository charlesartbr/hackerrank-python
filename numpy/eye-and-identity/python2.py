import numpy

n, m = map(int, raw_input().split())

# to fix the ouput format
numpy.set_printoptions(sign=' ')

print numpy.eye(n, m)