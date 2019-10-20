n = int(input())
ns = set(map(int, input().split()))
b = int(input())
bs = set(map(int, input().split()))

print(len(ns - bs))