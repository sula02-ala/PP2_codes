a=int(input())

i=0
b=[]

while(i<a):
    c=input()
    b.append(c)
    i=i+1

result=set(b)

print(len(result))                    
