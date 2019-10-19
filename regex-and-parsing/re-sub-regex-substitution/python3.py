import re

for _ in range(int(input())):

    text = input()

    for s, r in [('\&\&', 'and'), ('\|\|', 'or')]:
        text = re.sub(r"(?<= )(" + s + ")(?= )", r, text)

    print(text)
