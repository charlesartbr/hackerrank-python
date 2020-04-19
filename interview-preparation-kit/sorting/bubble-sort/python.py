def countSwaps(a):

    swaps = 0

    for i in range(len(a)):
        for j in range(len(a) - 1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    print('Array is sorted in %d swaps.' % swaps)
    print('First Element: %d' % a[0])
    print('Last Element: %d' % a[len(a)-1])

n = int(input())
a = list(map(int, input().rstrip().split()))

countSwaps(a)