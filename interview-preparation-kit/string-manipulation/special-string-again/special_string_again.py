def substrCount(n, s):

    specials = n

    for i in range(n):
        
        diff = False
        buffer = 0
        
        for j in range(i + 1, n):
               
            if diff == True:
               
                if s[i] == s[j]:

                    buffer = buffer - 1

                    if buffer == 0:
                        specials = specials + 1
                        break
                else:
                    break

            else: 

                buffer = buffer + 1

                if s[i] == s[j]:
                    specials = specials + 1
                else:
                    if diff == False:
                        diff = True
                    else:
                        break

    return specials

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = substrCount(n, s)

    print(result)