import re

n = int(raw_input())

css = ''

for _ in xrange(n):

    css += raw_input()

matches = re.findall(r"\{[^\}]*\}", css)

for match in matches:

    colors = re.findall(r"(#[0-9a-f]{6}|#[0-9a-f]{3})", match, re.IGNORECASE)

    for color in colors:
        
        print color