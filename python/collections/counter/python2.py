from collections import Counter

x = int(raw_input())
shoes = Counter(map(int, raw_input().split()))
n = int(raw_input())

total = 0

for _ in xrange(n):
    size, price = map(int, raw_input().split())
    if shoes[size] > 0:
        total += price
        shoes[size] -= 1

print total
