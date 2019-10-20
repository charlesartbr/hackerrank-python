from collections import defaultdict

d = defaultdict(list)

n, m = map(int, input().split())

[d[input()].append(str(i + 1)) for i in range(n)]
    
for i in range(m):
    s = input()
    print(' '.join(d[s]) if len(d[s]) > 0 else '-1')