if __name__ == '__main__':

    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

    coords = []

    for nx in range(x + 1):
        for ny in range(y + 1):
            for nz in range(z + 1):
                if nx + ny + nz != n:
                    coords.append([nx, ny, nz])

    print coords
    