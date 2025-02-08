N,S,E = map(int,input().split())

D = list(map(int,input().split()))
range = D[S-1:E]
sum_price = sum(range)
# 結果を出力
print(sum_price)
