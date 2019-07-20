import numpy

n, m = map(int, raw_input().split())

arrA = []
arrB = []

for _ in xrange(n):
    arrA.append(map(int, raw_input().split()))

for _ in xrange(n):
    arrB.append(map(int, raw_input().split()))

a = numpy.array(arrA)
b = numpy.array(arrB)

print numpy.add(a, b)
print numpy.subtract(a, b)
print numpy.multiply(a, b)
print numpy.divide(a, b)
print numpy.mod(a, b)
print numpy.power(a, b)