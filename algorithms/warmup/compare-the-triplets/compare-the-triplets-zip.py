def compareTriplets(a, b):
    return [
        sum(map(lambda x: x[0] > x[1], zip(a, b))),
        sum(map(lambda x: x[1] > x[0], zip(a, b)))
    ]

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

print(' '.join(map(str, result)))

# Explanation:

# zip(a, b): return for each iteration an array with one element of "a" and one of "b";
# map(lambda x: x[0] > x[1]): return 1 when "a > b" and 0 when "b > a";
# sum(): sum all the items.

# Note 