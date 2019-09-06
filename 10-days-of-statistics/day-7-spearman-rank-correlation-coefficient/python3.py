n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

sx = sorted(x)
sy = sorted(y)

d = sum(((sx.index(x[i]) + 1) - (sy.index(y[i]) + 1)) ** 2 for i in range(n))

s = 1 - ((6 * d) / (n * ((n ** 2) - 1)))

print(round(s, 3))