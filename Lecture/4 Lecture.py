# import statistics
# print(statistics.mean([85,90]))

# import random
# coin=random.choice([1,2,3,4,5,6])
# print(coin)

# import random
# cards=["clubs","diamonts","Heart","spades"]
# random.shuffle(cards)
# for card in cards:
#     print(card)

# import sys
# try:
#     print("Hello,my name is",sys.argv[3])
# except IndexError:
#     print("Woops,index is wrong!")

# import sys
# try:
#     sys.exit("Hello,my name is",sys.argv[3])
# except IndexError:
#     sys.exit("Woops,index is wrong!")

# import re
# p=re.compile('kaz{5}')

# word='kazzzzz'

# print(p.match(word))


import json

data = {
    "students": [
        {"name": "Ivan", "age": 20},
        {"name": "Anna", "age": 22}
    ]
}

for student in data["students"]:
    print(student["age"])