import re

txt = input()

def double_digit(match):
    d = match.group()
    return d * 2

result = re.sub(r"\d", double_digit, txt)

print(result)