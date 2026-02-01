a=int(input())

b={}

for i in range(1,a+1):
    c=input()
    if c not in b:
        b[c]=i

for c in sorted(b):
    print(c,b[c])

  
       