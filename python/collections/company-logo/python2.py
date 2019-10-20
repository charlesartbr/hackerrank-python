from collections import OrderedDict

company_name = raw_input()
letters = OrderedDict()

for c in company_name:

    if letters.has_key(c):
        letters[c] += 1
    else:
        letters[c] = 1

# sort by value DESC, then key ASC
s = sorted(letters.items(), key=lambda l: (-l[1], l[0]))

for i in xrange(3):
    print s[i][0], s[i][1]