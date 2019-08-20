from itertools import permutations
from fractions import Fraction

# all suits of cards
a = [1] * 13
b = [2] * 13
c = [3] * 13
d = [4] * 13

# permute all cards
p = list(permutations(a + b + c + d, 2))

# get only two equals
n = list(filter(lambda x: x[0] == x[1], p))

# result
r = Fraction(len(n), len(p))

# result 4/17
print(r)

# result 12/51 (HackerRank option)
print("%d/%d" % (r.numerator * 3, r.denominator * 3))