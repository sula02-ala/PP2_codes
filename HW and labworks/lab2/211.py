a,c,d=map(int,input().split())

b=list(map(int,input().split()))

c=c-1
d=d-1

while(c<d):
    b[c],b[d]=b[d],b[c]
    c=c+1
    d=d-1
for i in range(a):
    print(b[i],end=" ")    