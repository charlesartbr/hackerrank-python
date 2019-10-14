n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happiness = sum([1 if i in a else (-1 if i in b else 0) for i in arr])

print(happiness)