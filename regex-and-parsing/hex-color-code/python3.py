import re

css = str.join('', [input() for _ in range(int(input()))])

for match in re.findall(r"\{[^\}]*\}", css):

    [print(c) for c in re.findall(r"(#[0-9a-f]{6}|#[0-9a-f]{3})", match, re.I)]