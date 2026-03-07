import re

txt = input()

pattern = re.compile(r"\b\w+\b")

words = pattern.findall(txt)

print(len(words))