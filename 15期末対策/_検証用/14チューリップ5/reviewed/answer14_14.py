D = int(input())
K = input()
A = input()

R_L_tilt = 0

for player,window in range(K,A):
    match player:
        case 'L': R_L_tilt -= 1
        case 'R': R_L_tilt += 1
    match window:
        case 'L': R_L_tilt -= 1
        case 'R': R_L_tilt += 1
    if abs(R_L_tilt) > 3:
        print("YOU LOST")
        break
else:
    print("GOAL")