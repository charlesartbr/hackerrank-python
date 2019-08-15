n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

mw = sum(x[i] * w[i] for i in range(n))

print("%.1f" % (mw / sum(w)))