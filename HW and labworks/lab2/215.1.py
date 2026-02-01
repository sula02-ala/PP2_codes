a=int(input())

i=0
b=[]

while(i<a):
    c=input()
    b.append(c)
    i=i+1

result=[]
for d in range(a):
    if b[d] in result:
        continue
    else:
        result.append(b[d])

print(len(result))                    
