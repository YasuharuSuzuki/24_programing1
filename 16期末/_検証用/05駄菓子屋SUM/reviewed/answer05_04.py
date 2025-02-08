N, S, E = map(int,input().split())
Dn = list(map(int,input().split()))
goukei = sum(Dn[S-1:E])
print(goukei)