m = int(raw_input())
mArray = set(map(int, raw_input().split()))

n = int(raw_input())
nArray = set(map(int, raw_input().split()))

mDifference = mArray.difference(nArray)
nDifference = nArray.difference(mArray)

difference = map(str, sorted(mDifference | nDifference))

print '\n'.join(difference)