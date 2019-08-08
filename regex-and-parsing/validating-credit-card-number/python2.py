import re

n = input()

for _ in xrange(n):

    cc = raw_input()

    if re.search(r"^([456]\d{3})([ -]?\d{4}){3}$", cc):

        # remove non digits
        cc = re.sub(r"[^\d]", "", cc)
        
        if not re.search(r'(\d)\1{3}', cc):
            print 'Valid'
        else:
            print 'Invalid'

    else:
        print 'Invalid'