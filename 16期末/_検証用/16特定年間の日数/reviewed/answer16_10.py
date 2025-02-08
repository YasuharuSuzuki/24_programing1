a, b = map(int,input().split())
c = b - a
all = c * 365
wari = c / 4 + 1
i = c / 100 + 1
k = c / 400

e = wari - i + k

print(e + all)

