from itertools import product
from fractions import Fraction

# 1 for boy
# 0 for girl
x = [1, 0]
y = [0, 1]

# all combinations, excluded two girls
p = list(filter(lambda m: sum(m) > 0, product(x, y)))

# all combinations with two boys
e = list(filter(lambda m: sum(m) == 2, p))

# result: 1/3
print(Fraction(len(e), len(p)))