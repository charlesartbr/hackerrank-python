def fibonacci(n):
    if n <= 1:
        return n

    f = [0, 1]

    for x in range(2,n+1):
        f.append(f[x-2] + f[x-1])

    return f[n]

n = int(input())
print(fibonacci(n))