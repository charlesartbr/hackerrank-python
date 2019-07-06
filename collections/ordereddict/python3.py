from collections import OrderedDict

ordinary_dictionary = OrderedDict()

for _ in range(int(input())):

    data = input().split()
    price = int(data.pop())
    name = ' '.join(data)

    if name in ordinary_dictionary:
        ordinary_dictionary[name] += price
    else:
        ordinary_dictionary[name] = price

[print(item[0] + ' ' + str(item[1])) for item in ordinary_dictionary.items()]
    