import re

t = int(raw_input())

for _ in xrange(t):

    uid = raw_input()

    # It must contain at least 2 uppercase English alphabet characters.
    c1 = len(re.findall(r"[A-Z]", uid)) >= 2

    # It must contain at least 3 digits (0-9).
    c2 = len(re.findall(r"[0-9]", uid)) >= 3

    # It should only contain alphanumeric characters (a-z, A-Z & 0-9).
    c3 = len(re.findall(r"[a-zA-Z0-9]", uid)) == len(uid)

    # No character should repeat.
    c4 = len(set(uid)) == len(uid)

    # There must be exactly 10 characters in a valid UID.
    c5 = len(re.findall(r".", uid)) == 10

    # must be valid all conditions
    if c1 and c2 and c3 and c4 and c5:
        print 'Valid'
    else:
        print 'Invalid'