from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

combinations = list(map(tuple, combinations(range(1,n+1), k)))

has_a = sum(1 for c in combinations if 'a' in [letters[l-1] for l in list(c)])

print(has_a / len(combinations))