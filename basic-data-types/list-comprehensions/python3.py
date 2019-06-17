if __name__ == '__main__':

    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coords = [[nx, ny, nz] for nx in range(x + 1) 
                           for ny in range(y + 1) 
                           for nz in range(z + 1) 
                           if nx + ny + nz != n]

    print(coords)