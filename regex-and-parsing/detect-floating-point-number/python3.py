import re

pattern = r'^[\+-]{,1}\d*\.\d+$'

for _ in range(int(input())):
    
    print(True if re.search(pattern, input()) else False)
