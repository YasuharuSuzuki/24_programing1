chokkei = {
    1: 20.0,
    5: 22.0,
    10: 23.5,
    50 : 21.0,
    100: 22.6,
    500: 26.5}

A,B = map(int, input().split())

if chokkei[A] > chokkei[B]:
    print("A")

elif chokkei[A] < chokkei[B]:
    print("B")

else:
    print("同じ")
