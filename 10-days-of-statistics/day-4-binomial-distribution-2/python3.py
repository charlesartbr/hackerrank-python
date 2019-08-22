from math import factorial

ratio = 12.0 / 100
batch = 10

def binomial(n, p):
    x = 0
    for success in range(n, p + 1):
        b = factorial(batch) / (factorial(success) * factorial(batch - success))
        x += b * (ratio ** success) * ((1 - ratio) ** (batch - success))
    return x

print("%.3f" % binomial(0, 2))
print("%.3f" % binomial(2, batch))
