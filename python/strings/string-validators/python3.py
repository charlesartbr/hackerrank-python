if __name__ == '__main__':

    s = input()
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(len(list(filter(lambda c: eval('c.' + test + '()'), list(s)))) > 0)
