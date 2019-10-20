import numpy as np

# to fix the ouput format
np.set_printoptions(legacy='1.13')

arr = [list(map(float, input().split())) for _ in range(int(input()))]
    
print(np.linalg.det(arr))