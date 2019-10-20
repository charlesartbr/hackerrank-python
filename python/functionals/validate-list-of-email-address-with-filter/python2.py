import re

def fun(s):
    pattern = '^[a-z0-9-_]+@[a-z0-9]+\.[a-z]{1,3}$'
    return re.search(pattern, s, re.IGNORECASE)

def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails