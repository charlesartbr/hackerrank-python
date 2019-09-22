n = int(input())
b = ''

while True:
    b = str(n % 2) + b
    n = n // 2
    if n < 2:
        b = str(n) + b
        break

print(max(len(ones) for ones in b.split('0')))