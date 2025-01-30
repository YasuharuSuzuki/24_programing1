D = int(input())
K = input()
A = input()
tilt = 0

for action in K:
    match action:
        case 'L':  tilt -= 1
        case 'R':  tilt += 1
        case 'N':  tilt = tilt
    match A[0]:
        case 'L':  tilt -= 1
        case 'R':  tilt += 1
        case 'N':  tilt = tilt
if tilt > 3 or tilt < -3:
    print("YOU LOST")
else:
    print("GOAL")

