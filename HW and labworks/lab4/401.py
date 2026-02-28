

def square(a):
    for i in range(1,a+1):
        yield(i**2)

a=int(input())

gen=square(a)

for n in gen:
    print(n)