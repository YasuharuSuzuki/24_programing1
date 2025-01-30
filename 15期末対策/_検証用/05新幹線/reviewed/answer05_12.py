T, S = input().split()
match T:
    case "のぞみ":
        if S == "指定席":
            print(10000)
        elif S == "自由席":
            print(9500)
        elif S == "グリーン車":
            print(15000)
    case "ひかり":
        if S == "指定席":
            print(9000)
        elif S == "自由席":
            print(8500)
        elif S == "グリーン車":
            print(14000)
    case "こだま":
        if S == "指定席":
            print(8000)
        elif S == "自由席":
            print(7500)
        elif S == "グリーン車":
            print(13000)
