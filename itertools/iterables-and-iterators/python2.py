import itertools

n = input()
letters = raw_input().split()
k = input()

combinations = map(tuple, itertools.combinations(range(1,n+1), k))

has_a = 0

for c in combinations:
    for l in list(c):
        if letters[l - 1] == 'a':
            has_a += 1
            break

print float(has_a) / len(combinations)