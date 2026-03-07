import re

txt=input()
x=re.findall("^Hello",txt)

if x:
    print("Yes")
else:
    print("No")    