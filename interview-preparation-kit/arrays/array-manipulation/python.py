def arrayManipulation(n, queries):

    arr = [0] * (n + 1)
    max_value = 0
    x = 0

    for row in queries:

        start, end, value = row
        arr[start-1] += value

        if end < n:
            arr[end] -= value

    for i in range(n):
       x = x + arr[i]
       if max_value < x:
           max_value = x

    return max_value

n, m = map(int, input().split())

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)

print(result)