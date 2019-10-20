from collections import Counter

def sockMerchant(n, ar):

    socks = Counter()

    for sock in ar:
        socks[sock] += 1
    
    return int(sum((i - i % 2) / 2 for s, i in socks.items()))
        

n = int(input())
ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)

print(result)