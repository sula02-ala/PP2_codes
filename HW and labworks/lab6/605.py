S = input()

vowels = "aeiouAEIOU"

if any(c in vowels for c in S):
    print("Yes")
else:
    print("No")