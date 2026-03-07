import re

txt = input()

words = re.findall(r"\b[a-zA-Z]{3}\b", txt)

print(len(words))