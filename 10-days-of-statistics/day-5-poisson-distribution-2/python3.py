a, b = map(float, input().split())

ca = 160 + (40 * (a + a ** 2))
cb = 128 + (40 * (b + b ** 2))

print("%.3f" % ca)
print("%.3f" % cb)