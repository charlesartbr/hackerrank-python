import glob
from special_string_again import substrCount
    
for input in glob.glob("input*"):

    with open(input, 'r') as f:

        n = int(f.readline())

        s = f.readline()

        result = substrCount(n, s)

        print('\nTest:     ', input.replace('input', '').replace('.txt', ''))
        print('Lenght:   ', len(s))
        print('Output:   ', result)

        with open(input.replace('input', 'output'), 'r') as r:

            expected = r.readline()

            print('Expected: ', expected)
            print('Passed:   ', str(result) == expected)