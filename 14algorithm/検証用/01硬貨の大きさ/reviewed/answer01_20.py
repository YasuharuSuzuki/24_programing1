a, b = map(int, input().split())

match a:
    case 1:
        a_size = 20.0
    case 5:
        a_size = 22.0
    case 10:
        a_size = 23.5
    case 50:
        a_size = 21.0
    case 100:
        a_size = 22.6
    case 500:
        a_size = 26.5

match b:
    case 1:
        b_size = 20.0
    case 5:
        b_size = 22.0
    case 10:
        b_size = 23.5
    case 50:
        b_size = 21.0
    case 100:
        b_size = 22.6
    case 500:
        b_size = 26.5

if a_size > b_size:
    print("A")
elif a_size < b_size:
    print("B")
else:
    print("同じ")



