P=list(map(int,input().split()))
P.sort(reverse=True)
for ans in P[:3]:
    print(ans)