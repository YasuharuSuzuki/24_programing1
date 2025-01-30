T, S = input("").split()

kihonn = 0

if T == "のぞみ":
    kihon = 10000

elif T == "ひかり":
    kihon = 9000

else:
    kihon = 8000

if S == "自由席":
    kihon -= 500

elif S == "グリーン車":
    kihon += 5000

print(kihon)