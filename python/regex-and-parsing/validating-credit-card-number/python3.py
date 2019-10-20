import re

for _ in range(int(input())):

    cc = input()

    if re.search(r"^([456]\d{3})([ -]?\d{4}){3}$", cc):

        # remove non digits
        cc = re.sub(r"[^\d]", "", cc)
        
        print('Valid' if not re.search(r'(\d)\1{3}', cc) else 'Invalid')

    else:
        print('Invalid')