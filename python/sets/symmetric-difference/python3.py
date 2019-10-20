m = int(input())
mArray = set(map(int, input().split()))

n = int(input())
nArray = set(map(int, input().split()))

mDifference = mArray.difference(nArray)
nDifference = nArray.difference(mArray)

difference = map(str, sorted(mDifference | nDifference))

print('\n'.join(difference))