N,S,E = map(int,input().split())
D = list(map(int,input().split()))
sum_price = sum(D[S-1:E])
print(sum_price)

