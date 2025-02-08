N, S, E = map(int, input().split())
nedan = list(map(int, input().split()))
goukei = sum(nedan[S-1:E])
print(goukei)
