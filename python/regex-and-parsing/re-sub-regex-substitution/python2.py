import re

n = input()

for _ in xrange(n):

    text = raw_input()

    while re.search("(\s&&\s)", text):
        text = re.sub(r"(\s&&\s)", " and ", text)

    while re.search("(\s\|\|\s)", text):
        text = re.sub(r"(\s\|\|\s)", " or ", text)

    print text
