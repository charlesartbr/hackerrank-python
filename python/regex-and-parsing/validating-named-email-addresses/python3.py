import email.utils, re

pattern = '^[a-z][a-z0-9-_\.]*@[a-z]+\.[a-z]{1,3}$'

for _ in range(int(input())):

    parsed_address = email.utils.parseaddr(input())

    if re.search(pattern, parsed_address[1], re.I):
        print(email.utils.formataddr(parsed_address))