n = int(input())

s = [input() for _ in range(n)]

for i in range(n):
    even = ''.join([s[i][j] for j in range(0, len(s[i]), 2)])
    odd = ''.join([s[i][j] for j in range(1, len(s[i]), 2)])
    print(even, odd)
        