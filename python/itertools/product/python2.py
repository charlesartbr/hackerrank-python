from itertools import product

a = map(int, raw_input().split())
b = map(int, raw_input().split())

print str.join(' ', list(map(str, product(a, b))))