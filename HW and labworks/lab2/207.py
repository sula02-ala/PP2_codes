a=int(input())
b=list(map(int,input().split()))

max=b[0]
index=1
for i in range(a):
    if len(b)>1:
        if max<b[i]:
            max=b[i]
            index=i+1

print(index)