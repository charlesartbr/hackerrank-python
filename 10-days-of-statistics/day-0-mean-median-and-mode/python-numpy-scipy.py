import numpy as np
from scipy import stats

n = int(input())
v = list(map(int, input().split()))

# Mean:
print("%.1f" % np.mean(v))

#Median: 
print("%.1f" % np.median(v))

#Mode:
print("%.1f" % stats.mode(v)[0])