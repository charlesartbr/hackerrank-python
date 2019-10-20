from itertools import combinations

s, k = raw_input().split()

for i in xrange(int(k)):
    for p in sorted(map(lambda x: sorted(x), combinations(s, i + 1))):
        print ''.join(p)