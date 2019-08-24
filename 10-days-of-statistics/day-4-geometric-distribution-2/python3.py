denominator, numerator = map(float, input().split())
p = denominator / numerator
n = int(input())
q = 1 - p

r = sum((q ** i) * p for i in range(n))

print("%.3f" % r)