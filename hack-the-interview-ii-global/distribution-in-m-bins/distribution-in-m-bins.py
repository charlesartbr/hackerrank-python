def maxScore(a, m):

    a = sorted(a)
    score = 0
    segments = len(a) // m
    
    for i in range(segments):
        
        if i + 1 == segments:
            s = a[(i*m):]
        else:    
            s = a[(i*m):(i*m)+m]
        
        score += sum(s) * (i+1)
    
    return score % 1000000007

n, m = map(int, input().rstrip().split())

a = list(map(int, input().rstrip().split()))

ans = maxScore(a, m)

print(str(ans) + '\n')