def order_function(x):
    if x.islower():
        return (1, x)
    elif x.isupper():
        return (2, x)
    else:
        return (3 if int(x) % 2 == 1 else 4, x)

print(*sorted(input(), key = order_function), sep='')
