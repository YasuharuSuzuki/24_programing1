N, S, E = map(int,input().split())
D = list(map(int,input().split()))
print(sum(D[S-1:E]))