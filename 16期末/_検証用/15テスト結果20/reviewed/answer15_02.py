P = list(map(int,input().split()))

for i in range(3):
    print(max(P))
    P.pop(P.index(max(P)))
