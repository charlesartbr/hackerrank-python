from itertools import permutations
from fractions import Fraction

# 1 for red
# 0 for blue
x = [1, 1, 1]
y = [0, 0, 0, 0]

# all combinations, excluded first blue
p = list(filter(lambda m: m[0] == 1, permutations(x + y, 2)))

# all combinations with second blue
e = list(filter(lambda m: m[1] == 0, p))

# result: 2/3
print(Fraction(len(e), len(p)))