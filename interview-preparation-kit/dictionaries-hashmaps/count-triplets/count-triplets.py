from math import factorial

def countTriplets(arr, r):

    triplets = 0
    triplets_dict = {}

    for i in reversed(arr):

        if i in triplets_dict:
            triplets_dict[i] += 1
        else:
            triplets_dict[i] = 1

        r1 = i * r

        if r1 in triplets_dict:

            r2 = i * r * r

            if r2 in triplets_dict:

                triplets += triplets_dict[r1] * triplets_dict[r2]

    return triplets


n, r = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))

ans = countTriplets(arr, r)

print(ans)
