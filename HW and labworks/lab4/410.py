a=list(map(int,input().split()))
b=int(input())

def cycle(b):
    for i in range((len(a)*b)):
        yield(a[i%len(a)])

gen=cycle(b)     

for n in gen:
    print(n,end=" ")


