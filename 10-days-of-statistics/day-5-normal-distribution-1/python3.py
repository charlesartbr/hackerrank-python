import math

mean, std = map(float, input().split())

t1 = float(input())
t2, t3 = map(float, input().split())

def normal_distribution(x, mean, std):
    return (1/std) + (1/std) * math.erf((x-mean)/(std* 2**(1/std)))

print("%.3f" % normal_distribution(t1, mean, std))
print("%.3f" % (normal_distribution(t3, mean, std) - normal_distribution(t2, mean, std)))