def rotLeft(a, d):

    for i in range(d):
        a = a[1:] + [a[0]]

    return a

n, d = map(int, input().split())
a = list(map(int, input().rstrip().split()))

result = rotLeft(a, d)

print(' '.join(map(str, result)))