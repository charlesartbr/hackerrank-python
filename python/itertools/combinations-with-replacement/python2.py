from itertools import combinations_with_replacement

s, k = raw_input().split()

for p in sorted(map(lambda x: sorted(x), combinations_with_replacement(s, int(k)))):
    print ''.join(p)