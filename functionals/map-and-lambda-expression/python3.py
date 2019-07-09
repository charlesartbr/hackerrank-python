cube = lambda x: x ** 3

def fibonacci(n):
    
    f = [0, 1]

    if n < 2:
        return f[:n]

    for i in range(n - 2):
        f.append(f[i] + f[i + 1])

    return f

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))