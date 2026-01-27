a=int(input())

b=list(map(int,input().split()))

max=b[0]
min=b[0]

for i in range(a):
    if max<b[i]:
        max=b[i]

for i in range(a):
    if min>b[i]:
        min=b[i]

for i in range(a):
    if b[i]==max:
        b[i]=min

for i in range(a):
    print(b[i],end=" ")                 