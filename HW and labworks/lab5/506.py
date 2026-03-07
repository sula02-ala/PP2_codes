import re

txt=input()

x=re.search(r"\S+@\S+\.\S+", txt)

if x:
    print(x.group())
else:
    print("No email")    