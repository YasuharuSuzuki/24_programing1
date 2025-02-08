N, S, E = map(int,input().split())
D = list(map(int,input().split()))
kekka = sum(D[S-1:E])
print(kekka)