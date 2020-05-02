def luckBalance(k, contests):

    # sum all unimportants
    luck = sum(i[0] for i in contests if i[1] == 0)

    # separe important
    importants = sorted(filter(lambda x: x[1] == 1, contests), reverse=True)

    # sum important she can skip
    luck += sum(i[0] for i in importants[:k])

    # discount used luck
    luck -= sum(i[0] for i in importants[k:])

    return luck

n, k = map(int, input().split())

contests = []

for _ in range(n):
    contests.append(list(map(int, input().rstrip().split())))

result = luckBalance(k, contests)

print(result)
