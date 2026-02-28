a,b=list(map(int,input().split()))
sq = (x*x for x in range(a,b+1))
for i in sq:
    print(i)    