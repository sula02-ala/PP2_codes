
to_digit = {
    "ZER": "0",
    "ONE": "1",
    "TWO": "2",
    "THR": "3",
    "FOU": "4",
    "FIV": "5",
    "SIX": "6",
    "SEV": "7",
    "EIG": "8",
    "NIN": "9"
}


to_word = {
    "0": "ZER",
    "1": "ONE",
    "2": "TWO",
    "3": "THR",
    "4": "FOU",
    "5": "FIV",
    "6": "SIX",
    "7": "SEV",
    "8": "EIG",
    "9": "NIN"
}

s = input()


operator = ""
for ch in s:
    if ch == "+" or ch == "-" or ch == "*":
        operator = ch


left, right = s.split(operator)


num1 = ""
i = 0
while i < len(left):
    triple = left[i:i+3]
    num1 = num1 + to_digit[triple]
    i = i + 3


num2 = ""
i = 0
while i < len(right):
    triple = right[i:i+3]
    num2 = num2 + to_digit[triple]
    i = i + 3

num1 = int(num1)
num2 = int(num2)


if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
else:
    result = num1 * num2


result = str(result)
answer = ""

for digit in result:
    answer = answer + to_word[digit]

print(answer)
