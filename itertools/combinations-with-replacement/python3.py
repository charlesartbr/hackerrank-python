from itertools import combinations_with_replacement

s, k = input().split()

combinations = sorted(map(lambda x: sorted(x), combinations_with_replacement(s, int(k))))

[print(''.join(p)) for p in combinations]
    