for i in xrange(input()):
    
    n = input()
    
    cubes = list(map(int, raw_input().split()))
    
    stack = 2 ** 31

    for j in xrange(n):

        if cubes[0] >= cubes[len(cubes) - 1] and cubes[0] <= stack:
            stack = cubes.pop(0)
        elif cubes[len(cubes) - 1] <= stack:
            stack = cubes.pop()
        else:
            stack = 0
            break

    print('Yes' if stack > 0 else 'No')