a=int(input())

b=list(map(int,input().split()))

c=[]


for i in range(a):   
    if b[i] in c:
        print("NO")
    else:
        print("YES")
        c.append(b[i])    