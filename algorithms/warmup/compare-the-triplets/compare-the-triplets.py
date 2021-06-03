def compareTriplets(a, b):
    
    scores = [0, 0]
    
    for i in range(len(a)):
        if a[i] > b[i]:
            scores[0] = scores[0] + 1
        elif b[i] > a[i]:
            scores[1] = scores[1] + 1

    return scores

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

print(' '.join(map(str, result)))
