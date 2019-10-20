import re

s = raw_input()

pattern = r"(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])"

matches = re.findall(pattern, s, re.I)

if matches:
    for m in matches:
        print m
else:
    print -1
