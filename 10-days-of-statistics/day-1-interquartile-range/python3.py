n = int(input())
x = list(map(int, input().split()))
f = list(map(int, input().split()))

def median(median_v):
    median_n = len(median_v)
    if median_n % 2 == 0:
        return (median_v[median_n // 2] + median_v[(median_n // 2) - 1]) / 2
    else:
        return median_v[median_n // 2]

arr = []

for i in range(n):
    arr += [x[i] for _ in range(f[i])]

arr = sorted(arr)

m = len(arr) // 2

l = arr[:m]
u = arr[m + (1 if n % 2 == 1 else 0):]

print("%.1f" % (median(u) - median(l)))