from __future__ import division

n = input()
x = map(int, raw_input().split())
w = map(int, raw_input().split())

mw = []

for i in xrange(n):
    mw.append(x[i] * w[i])

print "%.1f" % (sum(mw) / sum(w))
