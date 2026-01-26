a=input()
b=0

for i in range(len(a)):
    if '0' <= a[i] <= '9':
        b += 1
        
if b==len(a):
    print("int")
else:
    print("str")                
