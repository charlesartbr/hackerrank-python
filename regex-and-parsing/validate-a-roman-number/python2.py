m = "M{,3}(CM){,1}"
d = "(D{,1}|CD)"
c = "C{,3}(XC){,1}"
l = "(L{,1}|XL)"
x = "X{,3}(IX){,1}"
i = "(V{,1}I{,3}|IV)"

regex_pattern = r"^%s%s%s%s%s%s$" % (m, d, c, l, x, i)

import re
print(str(bool(re.match(regex_pattern, raw_input()))))