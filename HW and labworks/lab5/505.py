import re

txt = input()

if re.search(r"^[A-Za-z].*[0-9]$", txt):
    print("Yes")
else:
    print("No")