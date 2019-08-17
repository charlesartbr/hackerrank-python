n = input()
x = map(int, raw_input().split())

# mean
m = sum(x) / n

d = []

for i in xrange(n):
    d.append((x[i] - m) ** 2)

deviation = (sum(d) / n) ** 0.5

print "%.1f" % deviation