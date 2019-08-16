n = input()
x = map(int, raw_input().split())
f = map(int, raw_input().split())

def mean(mean_v):
    mean_n = len(mean_v)
    if mean_n % 2 == 0:
        return (mean_v[mean_n // 2] + mean_v[(mean_n // 2) - 1]) / 2
    else:
        return mean_v[mean_n // 2]

arr = []

for i in xrange(n):
    arr += [x[i] for _ in xrange(f[i])]

arr = sorted(arr)

m = len(arr) // 2

l = arr[:m]
u = arr[m + (1 if n % 2 == 1 else 0):]

print "%.1f" % (mean(u) - mean(l))