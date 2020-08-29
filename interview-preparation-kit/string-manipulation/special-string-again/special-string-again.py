def substrCount(n, s):

    specials = n

    for i in range(n-1):

        sub = s[i:]
        lsub = len(sub)

        for j in range(2, lsub+1):
               
            substr = sub[:j]

            lsub = len(substr)
            lset = len(set(substr))

            if lset > 2:
                break
            elif lset == 1:              
                specials += 1
            elif lset == 2 and lsub % 2 == 1:

                mid = lsub // 2

                if len(set(substr[:mid])) > 1:
                    break
                elif len(set(substr[mid+1:])) > 1:                
                    break
                elif substr[0] != substr[mid]:
                    specials += 1
                    break

    return specials

n = int(input())
s = input()

result = substrCount(n, s)

print(str(result))