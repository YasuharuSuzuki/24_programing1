T,S = input().split()
kihon1 = 10000
kihon2 = 9000
kihon3 = 8000
if T == "のぞみ" and S == "指定席":
    print(int(kihon1))
elif T == "のぞみ" and S == "自由席":
    ryokin1 = kihon1 -500
    print(int(ryokin1))
elif T == "のぞみ" and S == "グリーン車":
    ryokin2 = kihon1 + 5000
    print(int(ryokin2))
elif T == "ひかり" and S == "指定席":
    print(int(kihon2))
elif T == "ひかり" and S == "自由席":
    ryokin3 = kihon2 - 500
    print(int(ryokin3))
elif T == "ひかり" and S == "グリーン車":
    ryokin4 = kihon2 + 5000
    print(int(ryokin4))
elif T == "こだま" and S == "指定席":
    print(int(kihon3))
elif T == "こだま" and S == "自由席":
    ryokin5 = kihon3 - 500
    print(int(ryokin5))
elif T == "こだま" and S == "グリーン車":
    ryokin6 = kihon3 + 5000
    print(int(ryokin6))