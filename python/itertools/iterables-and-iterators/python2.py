import itertools

n = input()
s = raw_input().split()
k = input()

combinations = map(tuple, itertools.combinations(s, k))

has_a = 0

for c in combinations:
    if 'a' in c:
        has_a += 1

print float(has_a) / len(combinations)