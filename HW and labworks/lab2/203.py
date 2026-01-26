a=int(input())
b = list(map(int, input().split()))

sum=0
for i in range(a):
    sum=sum+b[i]
print(sum)    