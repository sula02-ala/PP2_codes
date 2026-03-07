import re

txt=input()

digits=re.findall("[0-9]",txt)
for i in range(len(digits)):
    print(digits[i],end=" ")