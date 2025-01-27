A, B = map(int, input().split())

coin = {
    1: 20.0,
    5: 22.0,
    10: 23.5,
    50: 21.0,
    100: 22.6,
    500: 26.5
}

coin_A = coin[A]
coin_B = coin[B]

if coin_A > coin_B:
    print("A")
elif coin_A < coin_B:
    print("B")
else:
    print("同じ")
