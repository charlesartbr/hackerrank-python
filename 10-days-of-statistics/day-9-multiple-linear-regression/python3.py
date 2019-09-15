from sklearn import linear_model

m, n = map(int, input().split())

x = []
y = []

for i in range(n):
    temp = list(map(float, input().split()))
    y.append(temp.pop())
    x.append(temp)

q = int(input())
queries = [list(map(float, input().split())) for i in range(q)]

lm = linear_model.LinearRegression()

lm.fit(x, y)
   
for p in lm.predict(queries):
    print(round(p, 2))