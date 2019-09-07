x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

n = len(x)

mean_x = sum(x) / n
mean_y = sum(y) / n
square_x = sum(x[i] ** 2 for i in range(n))
product_xy = sum(x[i] * y[i] for i in range(n))

b = ((n * product_xy) - (sum(x) * sum(y))) / ((n * square_x) - (sum(x) ** 2))

a = mean_y - (b * mean_x)

score_x = 80

# regression line
score_y = a + (b * score_x)

print(round(score_y, 3))