import numpy as np

n = int(input())
x = list(map(int, input().split()))

print ("%.1f" % np.std(x))