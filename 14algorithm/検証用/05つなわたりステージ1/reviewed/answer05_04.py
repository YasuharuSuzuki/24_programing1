S = input()
R = 0
L = 0
i = 0
for i in range(20):
    if R == 4 or L == 4:
        print("YOU LOST")
        break
    elif S[i] == "R":
        R += 1
        L -= 1
        continue
    elif S[i] == "L":
        L += 1
        R -= 1
        continue
if i == 19:
    print("GOAL")
