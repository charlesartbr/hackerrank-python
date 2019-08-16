n = int(input())
x = list(map(int, input().split()))
f = list(map(int, input().split()))

def mean(mean_v):
    mean_n = len(mean_v)
    if mean_n % 2 == 0:
        return (mean_v[mean_n // 2] + mean_v[(mean_n // 2) - 1]) / 2
    else:
        return mean_v[mean_n // 2]

arr = []

for i in range(n):
    arr += [x[i] for _ in range(f[i])]

arr = sorted(arr)

m = len(arr) // 2

l = arr[:m]
u = arr[m + (1 if n % 2 == 1 else 0):]

print("%.1f" % (mean(u) - mean(l)))