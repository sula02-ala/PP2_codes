a=int(input())

def prime(a):  
    if a<=1:
            print("")
    else:
        for i in range(2,a+1):
            is_prime=True

            for n in range(2,i):
                if i%n==0:
                     is_prime=False
                     break

            if is_prime:
                 yield i
gen=prime(a)                 
for g in gen:
    print(g,end=" ")     