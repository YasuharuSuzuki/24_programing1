Y1, Y2 = map(int,input().split())
all_Y = list(range(Y1,Y2+1))
gouke = 0
for i in range(Y2 - Y1 + 1):
    if all_Y[i] % 4 == 0 and (all_Y[i] % 100 != 0 or all_Y[i] % 400 == 0):
        gouke += 366
    else:
        gouke += 365
print(gouke)