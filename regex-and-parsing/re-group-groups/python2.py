import re

s = raw_input()

pattern = r"(([a-z0-9])\2?(?:\2))+"

m = re.search(pattern, s)

if m:
    print m.groups()[1]
else:
    print '-1'