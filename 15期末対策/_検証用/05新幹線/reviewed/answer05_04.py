ressya,zaseki = map(str, input().split())
ryoukin = 0
if ressya == "のぞみ":
    ryoukin += 10000
elif ressya == "こだま":
    ryoukin += 8000
elif ressya == "ひかり":
    ryoukin += 9000

if zaseki == "指定席":
    print(ryoukin)
elif zaseki == "自由席":
    ryoukin -= 500
    print(ryoukin)
elif zaseki == "グリーン車":
    ryoukin += 5000
    print(ryoukin)
