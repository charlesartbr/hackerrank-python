import numpy

p = map(float, raw_input().split())
x = float(raw_input())

print numpy.polyval(p, x)
