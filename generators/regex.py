import re

str = "Chameleon, The (2010) "

x = re.search("(\d{4})", str)

if (x):
    print(x)
else:
    print("No match")
