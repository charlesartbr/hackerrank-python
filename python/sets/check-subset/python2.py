t = int(raw_input())

for _ in xrange(t):
        
    na = int(raw_input())
    a = set(map(int, raw_input().split()))
    
    nb = int(raw_input())
    b = set(map(int, raw_input().split()))

    print len(a.intersection(b)) == na