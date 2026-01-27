a=int(input())
b=list(map(int,input().split()))

max=b[0]

for i in range(a):

    if max<b[i]:
        max=b[i]

print(max)