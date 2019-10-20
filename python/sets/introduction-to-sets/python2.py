from __future__ import division

def average(array):

    arrayAsSet = set(array)

    total = sum(arrayAsSet)

    n = len(arrayAsSet)

    return total / n


if __name__ == '__main__':

    n = int(raw_input())

    arr = map(int, raw_input().split())

    result = average(arr)

    print result