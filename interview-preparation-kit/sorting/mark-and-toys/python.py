def maximumToys(prices, k):

    spended = 0
    toys = 0

    for price in sorted(prices):

        if spended + price > k:
            break
        else:
            spended += price
            toys += 1

    return toys

n, k = map(int, input().split())

prices = list(map(int, input().rstrip().split()))

result = maximumToys(prices, k)

print(result)