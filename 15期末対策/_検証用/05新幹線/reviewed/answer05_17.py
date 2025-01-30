T,S = input().split()
R = 0
if T == "のぞみ":
    R = 10000
elif T == "ひかり":
    R = 9000
elif T == "こだま":
    R = 8000
if S == "指定席":
    pass
elif S == "自由席":
    R -= 500
elif S == "グリーン車":
    R += 5000
print(R)