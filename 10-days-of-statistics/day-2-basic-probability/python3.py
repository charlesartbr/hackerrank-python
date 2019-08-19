from itertools import product
from fractions import Fraction

p = list(product([1,2,3,4,5,6], repeat=2))

c = len(p)

n = sum(1 for x in p if sum(x) <= 9)

print("%d / 6" % (n / c * 6))