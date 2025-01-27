coin_sizes = {
    "1": 20.0,
    "5": 22.0,
    "10": 23.5,
    "50": 21.0,
    "100": 22.6,
    "500": 26.5,
}

coin_a,coin_b = input().split()

size_a = coin_sizes.get(coin_a)
size_b = coin_sizes.get(coin_b)

if size_a > size_b:
    print("A")
elif size_a < size_b:
    print("B")
else:
    print("同じ")