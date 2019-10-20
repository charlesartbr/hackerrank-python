import re

for _ in range(int(input())):
    try:
        x = re.search(input(), '')
        print('True')
    except:
        print('False')