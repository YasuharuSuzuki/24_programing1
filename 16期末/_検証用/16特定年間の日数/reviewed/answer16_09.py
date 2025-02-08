y1, y2 = map(int, input(). split())
a = y2 - y1 + 1
b = 0
c = 0
for i in range(a):
    y = y1+i
    if y % 400 == 0:
        b += 1
    elif y % 100 == 0:
        c += 1
    elif y % 4 == 0:
        b += 1
    else:
        c += 1
    y += 1

日数 = b * 366 + c * 365
print(日数)

