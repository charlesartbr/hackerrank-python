import re

t = int(raw_input())

for _ in xrange(t):

    s = raw_input()

    try:
        x = re.search(s, '')
        print 'True'
    except:
        print 'False'