def swap_case(s):

    return ''.join([c.lower() if c.isupper() else c.upper() for c in s])

if __name__ == '__main__':