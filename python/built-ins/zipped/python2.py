n, x = map(int, raw_input().split())

scores = []

for i in xrange(x):
    scores.append(map(float, raw_input().split()))

scoresByStudents = zip(*scores)

for i in xrange(n):
    print sum(scoresByStudents[i]) / x