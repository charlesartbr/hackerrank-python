from sklearn import linear_model

m, n = map(int, input().split())

features = [[],[]]
Y = []

for i in range(n):
    x = list(map(float, input().split()))
    Y.append(x.pop())
    for j in range(m):
        features[j].append(x[j])

q = int(input())

queries = [list(map(float, input().split())) for i in range(q)]

lm = linear_model.LinearRegression()

for i in range(q):
    
    lm.fit(features, queries[i])
    
    a = lm.intercept_
    b = lm.coef_
    
    y = a + sum((features[j][i] * b[j]) for j in range(m))

    print(y)