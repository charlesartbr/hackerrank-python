def print_rangoli(size):

    width = size + (size - 1) * 3

    #top
    for i in xrange(size, 0, -1):

        line = chr(ord('a') + i - 1)

        for c in xrange(i, size):
            line = chr(ord('a') + c) + line

        for c in xrange(i, size):
            line = line + chr(ord('a') + c)

        print '-'.join(line).center(width, '-')

    #bottom    
    for i in xrange(1, size):

        line = chr(ord('a') + i)

        for c in xrange(i + 1, size):
            line = chr(ord('a') + c) + line

        for c in xrange(i + 1, size):
            line = line + chr(ord('a') + c)

        print '-'.join(line).center(width, '-')

if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)