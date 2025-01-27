A, B = map(int, input().split())
match A:
    case 1: a = 20
    case 5: a = 22
    case 10: a = 23.5
    case 50: a = 21
    case 100: a = 22.6
    case 500: a = 26.5
match B:
    case 1: b = 20
    case 5: b = 22
    case 10: b = 23.5
    case 50: b = 21
    case 100: b = 22.6
    case 500: b = 26.5
if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("同じ")