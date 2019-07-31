from itertools import combinations

n = int(input())
s = input().split()
k = int(input())

combinations = list(combinations(s, k))

has_a = sum(1 for c in combinations if 'a' in c)

print(has_a / len(combinations))