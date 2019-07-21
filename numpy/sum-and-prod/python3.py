import numpy as np

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

print(np.prod(np.sum(np.array(arr), axis = 0)))