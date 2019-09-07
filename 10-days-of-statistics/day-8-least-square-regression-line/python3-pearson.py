x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

n = len(x)

def std(v, n):
    d = [(i - (sum(v) / n)) ** 2 for i in v]
    return (sum(d) / n) ** 0.5

µx = sum(x) / n
µy = sum(y) / n

σx = std(x, n)
σy = std(y, n)

p = sum((x[i] - µx) * (y[i] - µy) for i in range(n)) / (n * σx * σy)

b = p * (σy / σx)
a = µy - (b * µx)

score_x = 80

# regression line
score_y = a + (b * score_x)

print(round(score_y, 3))