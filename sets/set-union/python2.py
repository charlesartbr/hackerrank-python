n = int(raw_input())
ns = set(map(int, raw_input().split()))
b = int(raw_input())
bs = set(map(int, raw_input().split()))

print len(ns.union(bs))