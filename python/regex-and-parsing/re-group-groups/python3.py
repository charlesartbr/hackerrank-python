import re

m = re.search(r"(?P<repeat>([a-z0-9])\2?(?:\2))+", input())

print(m.groupdict()['repeat'][0] if m else '-1')
