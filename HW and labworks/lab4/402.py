a=int(input())
last=(a//2)*2
sq = (x for x in range(0, a+1,2))
for i in sq:
    if i==last:
        print(i)
    else:
        print(i,end=",")    