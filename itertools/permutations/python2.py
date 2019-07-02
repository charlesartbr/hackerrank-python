from itertools import permutations

s, k = raw_input().split()

for p in sorted(list(permutations(s, int(k)))):
    print ''.join(p)