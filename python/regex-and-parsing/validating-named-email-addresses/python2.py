import email.utils, re

n = int(raw_input())

pattern = '^[a-z][a-z0-9-_\.]*@[a-z]+\.[a-z]{1,3}$'

for _ in xrange(n):

    parsed_address = email.utils.parseaddr(raw_input())

    if re.search(pattern, parsed_address[1], re.IGNORECASE):
        print email.utils.formataddr(parsed_address)