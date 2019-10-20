import numpy

a = map(float, raw_input().split())

# to fix the ouput format
numpy.set_printoptions(sign=' ')

print numpy.floor(a)
print numpy.ceil(a)
print numpy.rint(a)