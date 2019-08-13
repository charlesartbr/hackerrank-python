n = int(input())
v = list(map(int, input().split()))

# Mean:
print("%.1f" % (sum(v) / n))


#Median: 
v = sorted(v)

if n % 2 == 0:
    m = (v[n // 2] + v[(n // 2) - 1]) / 2
else:
    m = v[n // 2]

print("%.1f" % m)

#Mode:
mode = dict()

for i in range(n):
    if v[i] in mode:
        mode[v[i]] += 1
    else:
        mode[v[i]] = 1

mode = sorted(mode.items(), key=lambda x: (-x[1], x[0]))

print("%.1f" % mode[0][0])