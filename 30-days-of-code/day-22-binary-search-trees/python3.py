n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

total_swaps = 0

for i in range(n):

    swaps = 0

    for j in range(n-1):

        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            swaps += 1
            total_swaps += 1

    if swaps == 0:
        break

print('Array is sorted in %d swaps.' % total_swaps)
print('First Element:', a[0])
print('Last Element:', a[n-1])