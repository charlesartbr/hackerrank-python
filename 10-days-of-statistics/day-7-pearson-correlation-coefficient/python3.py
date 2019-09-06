n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

def std(v, n):
    d = [(i - (sum(v) / n)) ** 2 for i in v]
    return (sum(d) / n) ** 0.5

µx = sum(x) / n
µy = sum(y) / n

σx = std(x, n)
σy = std(y, n)

p = sum((x[i] - µx) * (y[i] - µy) for i in range(n)) / (n * σx * σy)

print(round(p, 3))