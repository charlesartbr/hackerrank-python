from itertools import product

k, m = map(int, input().split())

n = [list(map(int, input().split()))[1:] for _ in range(k)]

print(max(sum(map(lambda x: x**2, x)) % m for x in list(product(*n))))