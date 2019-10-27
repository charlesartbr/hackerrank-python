def minimumSwaps(arr):

    swaps = 0
    # create empty array
    pos = [0] * (len(arr) + 1)

    # store actual positions
    for p, j in enumerate(arr):
        pos[j] = p

    for n in range(len(arr)):

        # if the number is at the right place just skip
        if arr[n] == n + 1:
            continue

        # get the number position
        p = pos[n + 1]

        # swap
        arr[p], arr[n] = arr[n], arr[p]

        # update the position for the swaped number 
        pos[arr[p]] = p

        swaps += 1

    return swaps

n = int(input())
arr = list(map(int, input().rstrip().split()))

res = minimumSwaps(arr)

print(res)