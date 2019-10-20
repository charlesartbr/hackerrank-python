import re

regex_pattern = "^[789]{1}[0-9]{9}$"

[print("YES" if re.match(regex_pattern, input()) else "NO") for _ in range(int(input()))]