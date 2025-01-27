A, B = map(int, input().split())

if A == B:
    print("同じ")
else:
    a_size = 0
    match A:
        case 1: A_size = 20
        case 5: A_size = 22
        case 10: A_size = 23.5
        case 50: A_size = 21
        case 100: A_size = 22.6
        case 500: A_size = 26.5
    match B:
        case 1: B_size = 20
        case 5: B_size = 22
        case 10: B_size = 23.5
        case 50: B_size = 21
        case 100: B_size = 22.6
        case 500: B_size = 26.5
    if A_size > B_size:
        print("A")
    elif A_size < B_size:
        print("B")
    else:
        print("同じ")