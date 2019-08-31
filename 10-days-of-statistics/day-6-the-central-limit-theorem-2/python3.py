import math

ramaing = float(input())
tickets = float(input())
mean = float(input())
std = float(input())

def normal_distribution(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / std / math.sqrt(2)))

clt = normal_distribution(ramaing, mean * tickets, std * math.sqrt(tickets))

print("%.4f" % clt)