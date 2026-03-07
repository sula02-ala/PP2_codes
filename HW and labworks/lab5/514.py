import re

txt = input()

pattern = re.compile(r"^\d+$")

if pattern.fullmatch(txt):
    print("Match")
else:
    print("No match")