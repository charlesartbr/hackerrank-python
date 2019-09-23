arr = [list(map(int, input().rstrip().split())) for _ in range(6)]

sums = []

for i in range(4):
    for j in range(4):
        sums+=[sum(arr[i][j:j+3]+[arr[i+1][j+1]]+arr[i+2][j:j+3])]

print(max(sums))
