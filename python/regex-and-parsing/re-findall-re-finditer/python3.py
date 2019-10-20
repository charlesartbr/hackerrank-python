import re

c = 'qwrtypsdfghjklzxcvbnm'

pattern = r"(?<=[%s])([aeiou]{2,})[%s]" % (c, c)

matches = re.findall(pattern, input(), re.I)

print(str.join('\n', matches) if matches else -1)