import math

mean, std = map(float, input().split())

t1 = float(input())
t2 = float(input())

def normal_distribution(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * 2 ** 0.5)))

print("%.2f" % ((1 - normal_distribution(t1, mean, std)) * 100))
print("%.2f" % ((1 - normal_distribution(t2, mean, std)) * 100))
print("%.2f" % (normal_distribution(t2, mean, std) * 100))