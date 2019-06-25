def print_formatted(number):

    width = len("{0:b}".format(number)) + 1

    for i in xrange(1, number + 1):
        print "{0:d}".format(i).rjust(width - 1) + "{0:o}".format(i).rjust(width) + "{0:X}".format(i).rjust(width) + "{0:b}".format(i).rjust(width) 

if __name__ == '__main__':

    n = int(raw_input())

    print_formatted(n)