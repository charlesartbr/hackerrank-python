def minimumAbsoluteDifference(arr):
    
    min_diff = 10 ** 9

    arr = sorted(arr)

    for i in range(len(arr)):

        min_diff = min([min_diff, abs(arr[i] - arr[i-1])])

        if min_diff == 0:
            break

    return min_diff

n = int(input())

arr = list(map(int, input().rstrip().split()))

result = minimumAbsoluteDifference(arr)

print(result)