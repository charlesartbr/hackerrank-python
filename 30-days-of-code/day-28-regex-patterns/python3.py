import re

n = int(input())

names = []

for _ in range(n):

    name, email = input().split()

    if re.search(r'@gmail.com$', email):
        names.append(name)

print(*sorted(names), sep='\n')