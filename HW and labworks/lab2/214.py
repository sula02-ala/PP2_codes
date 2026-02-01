a=int(input())

b=list(map(int,input().split()))

git={}

for x in b: #проходимся по всем элементам
    if x in git: #есть ли число в словаре
        git[x]+=1
    else:
        git[x]=1

maxcount=0
number=b[0]

for x in b:
    if git[x]>maxcount:
        maxcount=git[x]
        number=x
    elif git[x]==maxcount and x<number:
        number=x

print(number)