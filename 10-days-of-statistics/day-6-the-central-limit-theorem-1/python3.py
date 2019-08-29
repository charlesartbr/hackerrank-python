import math

weight = float(input())
boxes = float(input())
mean = float(input())
std = float(input())

def normal_distribution(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / std / math.sqrt(2)))

clt = normal_distribution(weight, mean * boxes, std * math.sqrt(boxes))

print("%.4f" % clt)