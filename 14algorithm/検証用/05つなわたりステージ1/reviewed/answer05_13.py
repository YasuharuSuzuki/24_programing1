S = input()
left_tilt = 0
right_tilt = 0

for i in range(len(S)):
    if S[i] == 'L':
        left_tilt += 1
        right_tilt = max(0, right_tilt - 1)
    elif S[i] == 'R':
        right_tilt += 1
        left_tilt = max(0, left_tilt - 1)
    if left_tilt > 3 or right_tilt > 3:
        print("YOU LOST")
        break
    if i == len(S) - 1:
        print("GOAL")

