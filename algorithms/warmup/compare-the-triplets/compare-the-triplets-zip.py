def compareTriplets(a, b):
    return [
        len(list(filter(lambda x: x[0] > x[1], zip(a, b)))),
        len(list(filter(lambda x: x[1] > x[0], zip(a, b))))
    ]

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

print(' '.join(map(str, result)))

# Explanation:

# zip(a, b): return for each iteration an array with one element of "a" and one of "b";
# filter(lambda x: x[0] > x[1]): return all items where "a > b";
# filter(lambda x: x[1] > x[0]): return all items where "b > a";
# len(list()): count how many items was filtered.