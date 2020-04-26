from collections import Counter

a = input()
b = input()

res = len(a+b) - (sum((Counter(a) & Counter(b)).values()) * 2)

print(str(res))