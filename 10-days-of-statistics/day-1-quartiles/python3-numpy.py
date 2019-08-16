import numpy as np

n = int(input())
x = sorted(map(int, input().split()))
  
m = n // 2

l = x[:m]
u = x[m + (1 if n % 2 == 1 else 0):]

print(int(np.median(l)))
print(int(np.median(x)))
print(int(np.median(u)))