import math

samples = float(input())
mean = float(input())
std = float(input())
d = float(input())
z = float(input())

s = std / (samples ** 0.5)

print("%.2f" % (mean - s * z))
print("%.2f" % (mean + s * z))