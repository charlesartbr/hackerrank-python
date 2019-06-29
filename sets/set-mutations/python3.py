na = int(input())
a = set(map(int, input().split()))

n = int(input())

for _ in range(n):

    cmd, nb = input().split()
    b = set(map(int, input().split()))

    if cmd == 'update':
        a.update(b)
    elif cmd == 'intersection_update':
        a.intersection_update(b)
    elif cmd == 'difference_update':
        a.difference_update(b)
    elif cmd == 'symmetric_difference_update':
        a.symmetric_difference_update(b)

print(sum(a))