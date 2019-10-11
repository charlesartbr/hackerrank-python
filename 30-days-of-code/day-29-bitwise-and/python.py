t = int(raw_input())

for _ in xrange(t):
    
    n, k = map(int, raw_input().split())
    
    maxab = 0

    for a in xrange(n-1, 1, -1):

        for b in xrange(n, a, -1):

            ab = a&b

            if ab < k and ab > maxab:
                maxab = ab

            if maxab == k-1:
                break

        if maxab == k-1:
            break

    print(maxab)