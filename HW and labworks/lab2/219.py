a=int(input())

episodes={}

for i in range(a):
    s,k=input().split()
    k=int(k)

    if s in episodes:
        episodes[s]+=k
    else:
        episodes[s]=k

for s in sorted(episodes):
    print(s,episodes[s])