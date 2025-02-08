Ys, Ye = map(int,input().split())
s = 0
for i in range((Ye+1) - Ys):
    if (i % 4 == 0) and (i % 100 != 0 or i % 400 == 0):
        s += 366
    else:
        s += 365
print(s)