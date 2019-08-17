n = int(input())
x = list(map(int, input().split()))

d = [(i - (sum(x) / n)) ** 2 for i in x]

print ("%.1f" % (sum(d) / n) ** 0.5)