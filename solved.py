import os

def count_pythons(path):
    
    pythons = 0

    for entry in os.listdir(path):

        if entry.startswith('.'):
            continue

        fullpath = os.path.join(path, entry)
        
        if os.path.isdir(fullpath):
            if any(file.endswith('.py') for file in os.listdir(fullpath)):
                pythons += 1   
            else: 
                print(fullpath, pythons)
            pythons += count_pythons(fullpath)
        
    return pythons

print(count_pythons('.'))