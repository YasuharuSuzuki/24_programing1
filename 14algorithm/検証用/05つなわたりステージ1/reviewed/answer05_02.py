S = input()
judge = 0
FLG =0

for i in S:
    if i == "L":
        judge += -1
    elif i == "R":
        judge += 1
    else:
        judge += 0
    if (judge < -3)or(judge > 3):
        FLG = -1
        break
if FLG == -1:
    print("YOU LOST")
else:
    print("GOAL")