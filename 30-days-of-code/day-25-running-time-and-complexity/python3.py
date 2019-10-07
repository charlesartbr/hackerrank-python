n = int(input())

def prime(n):
    
    if n < 2 or (n % 2 == 0 and n > 2):
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

for _ in range(n):
    print('Prime' if prime(int(input())) else 'Not prime')