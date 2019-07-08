def palindromic(n):
    nlist = list(str(n))
    return str.join('', nlist) == str.join('', reversed(nlist))

input()
numbers = list(map(int, input().split()))

is_palindromic = [palindromic(x) for x in numbers]
is_positive = [x >= 0 for x in numbers]

print(all(is_positive) and any(is_palindromic))