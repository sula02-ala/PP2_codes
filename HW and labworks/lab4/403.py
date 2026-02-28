a=int(input())

sq = (x for x in range(0, a+1,12))
for i in sq:
    print(i,end=" ")