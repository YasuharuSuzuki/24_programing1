from pickle import TRUE
kaisu = input()
s = input()
kaze = input()
n = 0
flag = TRUE
for i in s:
    if i == "R":
        n += 1
    elif i == "L":
        n += -1
    for i in kaze:
        if i == "R":
            n += 1
        elif i == "L":
            n += -1
    if n <= -3 or n >= 3:
        print("YOU LOST")
        flag = False
    break
if flag == TRUE:
    print("GOAL")
