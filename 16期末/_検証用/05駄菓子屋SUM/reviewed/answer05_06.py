N, S, E = map(int, input().split())

D = list(map(int, input().split()))

kau = D[S-1:E]

goukei = sum(kau)

print(goukei)
