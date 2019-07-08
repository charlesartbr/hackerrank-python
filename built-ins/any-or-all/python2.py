def palindromic(n):
    nlist = list(str(n))
    return str.join('', nlist) == str.join('', reversed(nlist))

n = int(raw_input())
numbers = map(int, raw_input().split())

is_positive = [x >= 0 for x in numbers]
is_palindromic = [palindromic(x) for x in numbers]

print all(is_positive) and any(is_palindromic)