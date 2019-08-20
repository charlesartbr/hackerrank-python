from itertools import product
from collections import Counter
from fractions import Fraction

x = ['r', 'r', 'r', 'r', 'b', 'b', 'b']
y = ['r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b']
z = ['r', 'r', 'r', 'r', 'b', 'b', 'b', 'b']

p = list(product(x, y, z))

m = 0

for c in p:
    n = Counter(c)
    if n['r'] == 2 and n['b'] == 1:
        m += 1
        
print(Fraction(m, len(p)))

# result: 17/42