na = int(raw_input())
a = set(map(int, raw_input().split()))

n = int(raw_input())

for _ in xrange(n):

    cmd, nb = raw_input().split()
    b = set(map(int, raw_input().split()))

    if cmd == 'update':
        a.update(b)
    elif cmd == 'intersection_update':
        a.intersection_update(b)
    elif cmd == 'difference_update':
        a.difference_update(b)
    elif cmd == 'symmetric_difference_update':
        a.symmetric_difference_update(b)

print sum(a)