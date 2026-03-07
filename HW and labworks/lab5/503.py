import re

text = input()
pattern = input()

matches = re.findall(pattern, text)

print(len(matches))