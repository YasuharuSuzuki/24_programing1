Y1, Y2 = map(int,input().split())
tosi = 0
nissuu = 0
D4 = 0

tosi = Y2 - Y1 + 1
nissuu = tosi * 365

for i in range(Y1, Y2):
    if i % 400 == 0:

        D4 += 1
    elif i % 100 == 0:
        D4 -=1
    elif i % 4 == 0:
        D4 += 1


print(nissuu + (D4 - D400))