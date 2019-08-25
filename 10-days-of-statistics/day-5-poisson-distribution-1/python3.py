from math import factorial, exp

mean = float(input())
k = int(input())

poisson = ((mean ** k) * exp(-mean)) / factorial(k)

print("%.3f" % poisson)