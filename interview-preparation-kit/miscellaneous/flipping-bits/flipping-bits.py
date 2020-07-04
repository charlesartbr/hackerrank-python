def flippingBits(n):

    b = format(n, '032b')
    i = ''.join(['1' if c == '0' else '0' for c in b])

    return int(i, 2)


q = int(input())

for _ in range(q):

    n = int(input())

    result = flippingBits(n)

    print(result)