import re

txt = input()

words = re.findall("[A-Z]", txt)

print(len(words))