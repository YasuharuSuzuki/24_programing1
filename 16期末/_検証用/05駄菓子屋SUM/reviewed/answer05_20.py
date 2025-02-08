N, S, E = map(int, input().split())
prices = list(map(int, input().split()))
print(sum(prices[S-1:E]))

