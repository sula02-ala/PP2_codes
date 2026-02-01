a=int(input())

b={}
i=0

while(i<a):
    c=input()
    if len(c)==14:
        if c in b:
            b[c]+=1
        else:
            b[c]=1
    i=i+1
count=0

for number in b:
    if b[number]==3:
        count+=1

print(count)        