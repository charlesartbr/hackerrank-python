from collections import OrderedDict

company_name = input()
letters = OrderedDict()

for c in company_name:

    if c in letters:
        letters[c] += 1
    else:
        letters[c] = 1

# sort by value DESC, then key ASC
s = sorted(letters.items(), key=lambda l: (-l[1], l[0]))

[print(s[i][0], s[i][1]) for i in range(3)]