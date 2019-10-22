def jumpingOnClouds(c):
    
    jumps = 0
    current = 0
    
    for i in range(len(c) - 1, 0, -1):
        if c[i] == 0:
            last = i
            break

    while current < last:

        if current + 2 < len(c) and c[current + 2] == 0:
            current += 2
            jumps += 1
        elif c[current + 1] == 0:
            current += 1
            jumps += 1

    return jumps


n = int(input())
c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c)

print(result)
