a=int(input())
prime=True

if a<=1:
    print("No")
else:
    for i in range(2,a):
        if a%i==0:
            prime=False

if prime==True:
    print("Yes")
else:
    print("No")                
