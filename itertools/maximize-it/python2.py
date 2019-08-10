from itertools import product

k, m = map(int, raw_input().split())

n = list()

for _ in xrange(k):
    l = list(map(int, raw_input().split()))
    l.reverse()
    l.pop()
    n.append(l)

eq = list()

for x in list(product(*n)):
    eq.append(sum(map(lambda x: x ** 2, x)) % m)

print max(eq)