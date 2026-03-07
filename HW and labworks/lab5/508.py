import re

txt=input()
target=input()
x=re.split(target,txt)

print(",".join(x))