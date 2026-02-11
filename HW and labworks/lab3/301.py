def valid():
    a=int(input())
    s=str(a)
    count=0
    for i in range(len(s)):
        if int(s[i])%2==0:
            count+=1

    if count == len(s):
        print("Valid")
    else:
        print("Not valid")  

valid()                  