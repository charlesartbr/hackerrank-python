for _ in range(int(input())):
        
    na = int(input())
    a = set(map(int, input().split()))
    
    nb = int(input())
    b = set(map(int, input().split()))

    print(len(a.intersection(b)) == na)