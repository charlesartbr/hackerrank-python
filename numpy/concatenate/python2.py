import numpy

n, m, p = map(int, raw_input().split())

n_arr = [map(int, raw_input().split()) for _ in xrange(n)]
m_arr = [map(int, raw_input().split()) for _ in xrange(m)]

print numpy.concatenate((n_arr, m_arr))