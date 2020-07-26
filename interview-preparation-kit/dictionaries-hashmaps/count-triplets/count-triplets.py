def countTriplets(arr, r):

    triplets = 0
    num_counter = {}

    for i in range(len(arr)):

        n = arr[i]

        if n in num_counter:
            num_counter[n] += 1
        else:
            num_counter[n] = 1

    for n1 in num_counter:
        
        n2 = n1 * r
        n3 = n2 * r

        if n2 in num_counter and n3 in num_counter:

            if n1 == n2 and n1 == n3:
                triplets += (num_counter[n1] * (num_counter[n1]-1) * (num_counter[n3]-2)) // 6
            else:
                triplets += num_counter[n1] * num_counter[n2] * num_counter[n3]

    return triplets


n, r = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))

ans = countTriplets(arr, r)

print(ans)
