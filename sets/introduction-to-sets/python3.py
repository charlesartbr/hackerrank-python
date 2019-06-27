def average(array):

    arrayAsSet = set(array)

    return sum(arrayAsSet) / len(arrayAsSet)


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().split()))

    result = average(arr)

    print(result)