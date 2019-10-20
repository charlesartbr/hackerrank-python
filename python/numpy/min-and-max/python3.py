import numpy as np

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

print(np.max(np.min(np.array(arr), axis = 1)))