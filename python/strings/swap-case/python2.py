def swap_case(s):

    str = ''

    for c in s:
        str += c.lower() if c.isupper() else c.upper()

    return str

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result