def merge_the_tools(string, k):
    n = len(string)
    for i in xrange(0, n, k):
        u = []
        for j in string[i:i+k]:
            if not j in u:
                u.append(j)
        print ''.join(u)

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    