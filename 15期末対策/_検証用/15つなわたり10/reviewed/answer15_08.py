D = input()
A = input()
K = input()
tilt = 0

for action in A:
    match action:
        case 'L':  tilt -= 1
        case 'R':  tilt += 1
    for action in K:
        match action:
            case "L":  tilt += 1
            case "R":  tilt -= 1

    if abs(tilt) > 3:
        print("YOU LOST")
        break
else:
    print("GOAL")
