N,S,E = map(int,input().split())
D = list(map(int,input().split()))
sum =0
for i in range(S-1,E):
  sum += D[i]
print(sum)

