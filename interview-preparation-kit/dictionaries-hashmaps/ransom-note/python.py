from collections import defaultdict

def checkMagazine(magazine, note):

    m = defaultdict(list)

    for word in magazine:
        if word in m:
            m[word] += 1
        else:
            m[word] = 1

    for word in note:
        if word in m:
            if m[word] == 0:
                print('No')
                return
            else:
                m[word] -= 1
        else:
            print('No')
            return

    print('Yes')

m, n = map(int, input().split())

magazine = input().rstrip().split()

note = input().rstrip().split()

checkMagazine(magazine, note)