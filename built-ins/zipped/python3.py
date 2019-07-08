n, x = map(int, input().split())

scores = [map(float, input().split()) for _ in range(x)]

scoresByStudents = list(zip(*scores))

[print(sum(scoresByStudents[i]) / x) for i in range(n)]
    