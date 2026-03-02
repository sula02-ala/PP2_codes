a=input()
reversed_txt = a[::-1]

my=iter(reversed_txt)
for i in range(len(reversed_txt)):
    print(next(my),end="")