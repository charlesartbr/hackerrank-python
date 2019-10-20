def wrapper(f):
    def fun(l):
        for i in xrange(len(l)):
            p = len(l[i]) - 5
            l[i] = '+91 ' + l[i][p-5:p] + ' ' + l[i][p:]
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))

if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    sort_phone(l) 