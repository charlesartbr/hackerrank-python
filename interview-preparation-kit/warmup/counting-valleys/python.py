def countingValleys(n, s):

    level = 0
    valleys = 0

    for d in s:

        if d == 'U':
            if level == -1:
                valleys += 1
            level += 1
        else:
            level -= 1

    return valleys

n = int(input())
s = input()

print(countingValleys(n, s))