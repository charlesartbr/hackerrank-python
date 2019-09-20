from collections import defaultdict

phonebook = defaultdict(list)

n = int(input())

for _ in range(n):
    name, phone = input().split()
    phonebook[name] = phone

while True:
    
    try:
        name = input()
    
        if name in phonebook:
            print('%s=%s' % (name, phonebook[name]))
        else:
            print('Not found')

    except EOFError:
            break