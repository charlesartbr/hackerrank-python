from math import factorial

ratio = 1.09 / (1.09 + 1)

trials = 6

x = 0

for success in range(3, trials + 1):
    b = factorial(trials) / (factorial(success) * factorial(trials - success))
    x += b * (ratio ** success) * ((1 - ratio) ** (trials - success))

print("%.3f" % x)