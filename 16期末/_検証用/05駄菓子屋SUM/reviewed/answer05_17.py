N, S, E = map(int,input().split())
price = list(map(int,input().split()))
total_price = sum(price[S-1:E])
print(total_price)
