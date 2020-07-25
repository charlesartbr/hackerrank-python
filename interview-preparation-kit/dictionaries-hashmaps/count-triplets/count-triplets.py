def countTriplets(arr, r):

    triplets = 0
    first = 0

    n = len(arr)

    for i in range(n - 2):

        # if first > 0 and first == arr[i]:

        first = arr[i]
        second = first * r

        for j in range(i + 1, n - 1):

            if arr[j] == second:

                third = second * r

                for k in range(j + 1, n):

                    if arr[k] == third:
                        triplets += 1
                    elif arr[k] > third:
                        break

            elif arr[j] > second:
                break

    return triplets


n, r = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))

ans = countTriplets(arr, r)

print(ans)