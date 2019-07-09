import re

t = int(raw_input())

pattern = '^[\+-]{,1}\d*\.\d+$'

for _ in xrange(t):
    
    n = raw_input()
    
    if re.search(pattern, n):
        print True
    else:
        print False
