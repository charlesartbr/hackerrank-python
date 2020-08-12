import collections

c = collections.Counter(input())
v = list(c.values())
n = len(set(v))
d = list(c.items())

print('YES' if n==1 or (n==2 and (len([x for x in d if x[1] == 1])==1 or len([x for x in d if x[1] == v[0]+1])==1)) else 'NO')