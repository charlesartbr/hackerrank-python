t = int(raw_input())

for _ in xrange(t):

    try:

        a, b = map(int, raw_input().split())

        print a / b

    except ZeroDivisionError as e:

        print 'Error Code:', e

    except ValueError as e:

        print 'Error Code:', e