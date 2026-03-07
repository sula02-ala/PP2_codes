import re

txt = input()

dates = re.findall(r"\d{2}/\d{2}/\d{4}", txt)

print(len(dates))