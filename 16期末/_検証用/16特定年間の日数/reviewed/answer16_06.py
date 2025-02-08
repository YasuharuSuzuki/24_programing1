Ya, Yb = map(int, input().split())

nissuu = 0
for i in range(Ya, Yb+1):
    if i % 400 ==0:
        nissuu += 366

    elif i % 100 == 0:
        nissuu += 365

    elif i % 4 == 0:
        nissuu += 366

    else:
        nissuu += 365

print(nissuu)
