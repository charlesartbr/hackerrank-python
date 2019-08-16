import numpy as np

n = int(input())
x = list(map(int, input().split()))
f = list(map(int, input().split()))

arr = sorted([x[i] for i in range(n) for _ in range(f[i])])

m = n // 2

l = x[:m]
u = x[m + (1 if n % 2 == 1 else 0):]

print("%.1f" % (np.median(u) - np.median(l)))