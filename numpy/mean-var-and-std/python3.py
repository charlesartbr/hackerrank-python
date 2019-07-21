import numpy as np

n, m = map(int, input().split())

arr = np.array([list(map(int, input().split())) for _ in range(n)])

# to fix the ouput format
np.set_printoptions(legacy='1.13')

print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(np.std(arr))