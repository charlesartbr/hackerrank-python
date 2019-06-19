if __name__ == '__main__':

    s = raw_input()

    print len(filter(lambda c: c.isalnum(), list(s))) > 0
    print len(filter(lambda c: c.isalpha(), list(s))) > 0
    print len(filter(lambda c: c.isdigit(), list(s))) > 0
    print len(filter(lambda c: c.islower(), list(s))) > 0
    print len(filter(lambda c: c.isupper(), list(s))) > 0
