def print_rangoli(size):

    width = size + (size - 1) * 3

    #top
    for i in range(size, 0, -1):

        line = list(reversed([chr(ord('a') + c) for c in range(i, size)]))

        line.append(chr(ord('a') + i - 1))

        line += [chr(ord('a') + c) for c in range(i, size)]

        print('-'.join(map(str, line)).center(width, '-'))

    #bottom    
    for i in range(1, size):

        line = list(reversed([chr(ord('a') + c) for c in range(i + 1, size)]))
            
        line.append(chr(ord('a') + i))

        line += [chr(ord('a') + c) for c in range(i + 1, size)]

        print('-'.join(map(str, line)).center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)