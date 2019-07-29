from itertools import groupby

S = raw_input()

groups = []

for k, g in groupby(S):
    groups.append((len(list(g)), int(k)))

print str.join(' ', map(str, groups))