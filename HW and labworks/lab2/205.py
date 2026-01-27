a=int(input())

b=a
power=0
if a==1:
    print("YES")
    exit()
else:
    if a%2!=0:
        exit
    else:
        while(a>=2):
            a=a//2
            power=power+1

if b==2**power:
    print("YES")
else:
    print("NO")
            
       