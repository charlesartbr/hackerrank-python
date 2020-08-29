from math import factorial

def countTriplets(arr, r):

    triplets = 0
    singles = {}
    pairs = {}

    for n1 in reversed(arr):

        if n1 in singles:
            singles[n1] += 1
        else:
            singles[n1] = 1

        n2 = n1 * r

        if n2 in singles:
            if n1 in pairs:
                pairs[n1] += singles[n2]
            else:
                pairs[n1] = singles[n2]

        if n2 in pairs:
            triplets += pairs[n2]

    if r == 1:
        triplets -= sum(singles[x] ** 2 for x in singles)

    return triplets


n, r = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))

ans = countTriplets(arr, r)

print(ans)
