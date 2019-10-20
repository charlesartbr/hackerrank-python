from collections import Counter

k = int(raw_input())
rooms = Counter(map(int, raw_input().split()))

for x in rooms.items():
    if x[1] == 1:
        print x[0]
