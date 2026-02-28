def pow(a):
    for i in range(a+1):
        yield(2**i)

a=int(input()) 
gen=pow(a) 

for n in gen:
    print(n,end=" ")