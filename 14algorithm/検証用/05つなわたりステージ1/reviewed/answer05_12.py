S = input()

L = 0
R = 0
for i in range(20):
    if S[i] == 'L':
        L += 1
    elif S[i] == 'R':
        R += 1

    if S[i] == 'R':
        L -= 1
    elif S[i] == 'L':
        R -= 1

if R > 3:
    print("YOU LOST")
elif L > 3:
    print("YOU LOST")
else:
    print("GOAL")