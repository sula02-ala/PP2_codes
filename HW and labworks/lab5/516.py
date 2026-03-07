import re

txt = input()

match = re.search(r"Name: (.+), Age: (\d+)", txt)

if match:
    name = match.group(1)
    age = match.group(2)
    print(name, age)