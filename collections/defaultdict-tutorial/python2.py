from collections import defaultdict

d = defaultdict(list)

n, m = map(int, raw_input().split())

for i in xrange(n):
    d[raw_input()].append(str(i + 1))

for i in xrange(m):
    s = raw_input()
    if d.has_key(s):
        print ' '.join(d[s])
    else:
        print '-1'