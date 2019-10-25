n, d = map(int, input().split())
a = list(map(int, input().rstrip().split()))

print(' '.join(map(str, a[d:] + a[:d])))