from itertools import combinations

s, k = input().split()

for i in range(int(k)):
    [print(''.join(p)) for p in sorted(map(lambda x: sorted(x), combinations(s, i + 1)))]
