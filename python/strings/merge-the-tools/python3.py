def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        u = []
        print(''.join([j for j in string[i:i+k] if not (j in u or u.append(j))]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)