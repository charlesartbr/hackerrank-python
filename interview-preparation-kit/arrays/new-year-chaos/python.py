def minimumBribes(q):

    nswaps = 0
    n = len(q)
        
    for i in range(n, 1, -1):

        ia = max(i - 3, 0)
        ib = min(i + 3, n) 

        index = None

        for j in range(ia, ib):
            if q[j] == i:
                index = j
                break

        if index is None:
            print('Too chaotic')
            return

        if index + 1 < n and q[index] > q[index+1]:   
            nswaps += 1
            q[index], q[index+1] = q[index+1], q[index]
            index += 1
        else:
            continue

        if index + 1 < n and q[index] > q[index+1]:
            nswaps += 1
            q[index], q[index+1] = q[index+1], q[index]
            index += 1
        else:
            continue

    if q == [i+1 for i in range(n)]:
        print(nswaps)
    else:
        print('Too chaotic')

t = int(input())

for t_itr in range(t):

    n = int(input())
    q = list(map(int, input().rstrip().split()))

    minimumBribes(q)
