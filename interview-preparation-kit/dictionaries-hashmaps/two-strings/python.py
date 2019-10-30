def twoStrings(s1, s2):
    
    for c in s1:
        if c in s2:
            return 'YES'

    return 'NO'

q = int(input())

for _ in range(q):

    s1 = input()
    s2 = input()

    result = twoStrings(s1, s2)

    print(result)