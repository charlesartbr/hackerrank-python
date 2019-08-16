n = int(input())
x = sorted(map(int, input().split()))

def mean(mean_v):
    mean_n = len(mean_v)
    if mean_n % 2 == 0:
        return int((mean_v[mean_n // 2] + mean_v[(mean_n // 2) - 1]) / 2)
    else:
        return int(mean_v[mean_n // 2])
    
m = n // 2

l = x[:m]
u = x[m + (1 if n % 2 == 1 else 0):]

print(mean(l))
print(mean(x))
print(mean(u))