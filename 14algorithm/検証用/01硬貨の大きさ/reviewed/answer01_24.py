A,B = map(int,input().split())
match A:
    case 1: C = (20.0)
    case 5: C = (22.0)
    case 10: C = (23.5)
    case 50: C = (21.0)
    case 100: C = (22.6)
    case 500: C = (26.5)
match B:
    case 1: D = (20.0)
    case 5: D = (22.0)
    case 10: D = (23.5)
    case 50: D = (21.0)
    case 100: D = (22.6)
    case 500: D = (26.5)
if C < D:
    print("B")
elif C > D:
    print("A")
else:
    print("同じ")

