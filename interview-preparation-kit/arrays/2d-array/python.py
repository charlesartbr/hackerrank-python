def hourglassSum(arr):

    n = len(arr)
    sums = []

    for i in range(n-2):
        for j in range(n-2):
            sums.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                        arr[i+1][j+1] + 
                        arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])

    return max(sums)

arr = [list(map(int, input().rstrip().split())) for _ in range(6)]

result = hourglassSum(arr)

print(result)