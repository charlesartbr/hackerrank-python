import re

n, m = map(int, raw_input().split())

matrix = []

for _ in xrange(n):
    matrix_item = raw_input()
    matrix.append(matrix_item)

traversed = []

for i in xrange(m):
    for j in xrange(n):
        traversed.append(matrix[j][i])

pattern = r'([a-zA-Z0-9])([^a-zA-Z0-9]+)([a-zA-Z0-9])'

decoded = re.sub(pattern, r'\1 \3', str.join('', traversed)) 

print decoded