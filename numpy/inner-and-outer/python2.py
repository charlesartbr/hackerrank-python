import numpy

a = map(int, raw_input().split())
b = map(int, raw_input().split())

print numpy.inner(a, b)
print numpy.outer(a, b)