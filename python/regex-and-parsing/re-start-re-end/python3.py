import re

s = input()
k = input()

matches = list(map(lambda x: x, re.finditer(r"(?=%s)" % k, s)))

if matches:
    for m in matches:
        print((m.start(), m.start() + len(k) - 1))
else:
    print((-1, -1))