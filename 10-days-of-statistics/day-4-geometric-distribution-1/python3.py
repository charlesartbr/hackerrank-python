denominator, numerator = map(float, input().split())
p = denominator / numerator
n = int(input())
q = 1 - p

r = (q ** (n - 1)) * p

print("%.3f" % r)