from collections import OrderedDict

ordinary_dictionary = OrderedDict()

n = int(raw_input())

for _ in xrange(n):
    data = raw_input().split()
    price = int(data.pop())
    name = ' '.join(data)

    if ordinary_dictionary.has_key(name):
        ordinary_dictionary[name] += price
    else:
        ordinary_dictionary[name] = price

for item in ordinary_dictionary.items():
    print item[0] + ' ' + str(item[1])