import re

n, m = map(int, input().split())

matrix = [input() for _ in range(n)]

traversed = [matrix[j][i] for i in range(m) for j in range(n)]

pattern = r'([a-z0-9])([^a-z0-9]+)([a-z0-9])'

decoded = re.sub(pattern, r'\1 \3', str.join('', traversed), 0, re.I) 

print(decoded)