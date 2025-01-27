S = input()
left = 0
right = 0

for i in range(len(S)):
    if S[i] == 'L':
        left += 1
        if right > 0:
            right -= 1
    elif S[i] == 'R':
        right += 1
        if left > 0:
            left -= 1

if left > 3 or right > 3:
    print("YOU LOST")
else:
    print("GOAL")