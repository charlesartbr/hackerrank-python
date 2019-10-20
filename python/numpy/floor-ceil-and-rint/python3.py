import numpy as np

a = list(map(float, input().split()))

# to fix the ouput format
np.set_printoptions(sign=' ')

print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))