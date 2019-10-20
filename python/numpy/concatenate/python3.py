import numpy

n, m, p = map(int, input().split())

n_arr = [list(map(int, input().split())) for _ in range(n)]
m_arr = [list(map(int, input().split())) for _ in range(m)]

print(numpy.concatenate((n_arr, m_arr)))