from collections import Counter

k = int(input())
rooms = Counter(map(int, input().split()))

for x in rooms.items():
    if x[1] == 1:
        print(x[0])