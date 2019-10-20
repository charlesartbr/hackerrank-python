import re

n = int(raw_input())

regex_pattern = "^[789]{1}[0-9]{9}$"

for _ in xrange(n):

    phone = raw_input()

    if re.match(regex_pattern, phone):
        print "YES"
    else:
        print "NO"