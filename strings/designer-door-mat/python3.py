n, m = map(int, input().split(' '))

# top 
for i in range(1, (n // 2) + 1):  
    print(('.|.' * ((i * 2) - 1)).center(m, '-'))  
    
# welcome  
print('WELCOME'.center(m, '-'))  

# bottom  
for i in range(((n - 1) // 2), 0, -1):  
    print(('.|.' * ((i * 2) - 1)).center(m, '-'))  