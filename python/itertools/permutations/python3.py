from itertools import permutations

s, k = input().split()

[print(''.join(p)) for p in sorted(list(permutations(s, int(k))))]