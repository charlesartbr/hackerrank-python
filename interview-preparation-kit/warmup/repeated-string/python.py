def count_a(s):
    return len(list(filter(lambda c: c == 'a', s)))

def repeatedString(s, n):

    a = count_a(s)
    x = n // len(s)

    return (a * x) + count_a(s[:(n - (x * len(s)))])

s = input()
n = int(input())

result = repeatedString(s, n)

print(result)