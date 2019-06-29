a = set(map(int, input().split()))
n = int(input())

is_super_set = True

for _ in range(n):
        
    b = set(map(int, input().split()))

    if len(b.intersection(a)) != len(b):
        is_super_set = False

print(is_super_set)