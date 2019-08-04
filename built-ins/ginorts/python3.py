def order_function(x):
    if x.islower():
        return ord(x)
    elif x.isupper():
        return ord(x) + 100
    else:
        return int(x) + (1000 if int(x) % 2 == 1 else 2000)

s = list(input())

print(str.join('', sorted(s, key = order_function)))