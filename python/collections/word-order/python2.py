from collections import OrderedDict

n = input()
words = OrderedDict()

for _ in xrange(n):

    word = raw_input()

    if words.has_key(word):
        words[word] += 1
    else:
        words[word] = 1

print len(words)

print str.join(' ', [str(item[1]) for item in words.items()])