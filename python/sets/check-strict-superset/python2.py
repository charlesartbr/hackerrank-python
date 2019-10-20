a = set(map(int, raw_input().split()))
n = int(raw_input())

is_super_set = True

for _ in xrange(n):
        
    b = set(map(int, raw_input().split()))

    if len(b.intersection(a)) <> len(b):
        is_super_set = False

print is_super_set