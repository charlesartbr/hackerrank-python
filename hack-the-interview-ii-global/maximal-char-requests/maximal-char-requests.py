from collections import Counter

def getMaxCharCount(s, queries):
    
    result = []
    
    s = s.lower()
    
    for query in queries:
        
        interval = s[query[0]:query[1]+1]
        
        char_counter = Counter(interval)
        
        interval_set = sorted(set(interval))

        result.append(char_counter[interval_set[-1]])

    return result
        

n = int(input().strip())
s = input()
q = int(input().strip())

query = []

for _ in range(q):
    query.append(list(map(int, input().rstrip().split())))

ans = getMaxCharCount(s, query)

print('\n'.join(map(str, ans)))