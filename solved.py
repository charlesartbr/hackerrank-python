import os

def count_solved(path):
    
    solved = 0

    for entry in os.listdir(path):

        if entry.startswith('.'):
            continue

        fullpath = os.path.join(path, entry)
        
        if os.path.isdir(fullpath):

            if any(file.endswith('.py') for file in os.listdir(fullpath)):
                solved += 1   

            solved += count_solved(fullpath)
        
    return solved

solved = count_solved('.')

txt = 'challenges solved'

print(solved, txt)

with open("README.md", "r") as readme:
    lines = []
    for line in readme:
        if txt in line:
            lines.append('### **' + str(solved) + '** ' + txt + ':\n')
        else:
            lines.append(line)

with open("README.md", "w") as readme:
    readme.writelines(lines)

        

