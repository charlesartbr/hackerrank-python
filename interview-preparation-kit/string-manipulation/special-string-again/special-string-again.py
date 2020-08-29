def is_special(s):

    lens = len(s)
    lenset = len(set(s))
    
    if lenset  == 1:
        return True

    if lens % 2 == 1 and lenset == 2 and s[lens // 2] != s[0]:
        return True

    return False

def substrCount(n, s):

    specials = n

    for i in range(n-1):
        for j in range(i+2, n+1):
            specials += is_special(s[i:j])

    return specials

n = int(input())
s = input()

result = substrCount(n, s)

print(str(result) + '\n')