def compareTriplets(a, b):
    return [
        sum(map(lambda x, y: x > y, a, b)),
        sum(map(lambda x, y: y > x, a, b))
    ]

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

print(' '.join(map(str, result)))

# Explanation:

# map(lambda x, y: x > y): return 1 when "a > b" and 0 when "b > a";
# sum(): sum all the items.
