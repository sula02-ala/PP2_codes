import re

txt=input()
target=input()
x=re.findall(target,txt)

if x:
    print("Yes")
else:
    print("No")    