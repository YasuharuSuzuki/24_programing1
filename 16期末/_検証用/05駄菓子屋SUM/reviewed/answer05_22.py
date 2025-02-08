N,S,E = map(int, input().split())
prices = list(map(int, input().split()))

total = sum(prices[S-1:E])

print(total)


