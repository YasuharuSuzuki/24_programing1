T , S = input().split()
match T:
    case "のぞみ":
        satand = 10000
    case "ひかり":
        satand = 9000
    case "こだま":
        satand = 8000

match S:
    case "指定席":
        print(satand)
    case "自由席":
        print(satand - 500)
    case "グリーン車":
        print(satand + 5000)