n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

s = sorted(arr, key = lambda x: x[k])

[print(str.join(' ', map(str, s[i]))) for i in range(n)]