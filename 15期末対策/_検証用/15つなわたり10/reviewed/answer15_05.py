D = int(input())
K = input()
A = input()
barance = 0
for ak in range(D):
    match K:
        case 'L':
            barance += 1
        case 'R':
            barance -= 1
    match A:
        case 'L':
            barance += 1
        case 'R':
            barance -= 1
    if abs(barance) > 3:
        print("YOU LOST")
        break
else:
    print("GOAL")