N, S, E = map(int,input().split())
tans = list(map(int,input().split()))

print(sum(tans[S-1:E]))


