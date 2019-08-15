import numpy as np

n = input()
x = map(int, raw_input().split())
w = map(int, raw_input().split())

print "%.1f" % np.average(x, weights=w)