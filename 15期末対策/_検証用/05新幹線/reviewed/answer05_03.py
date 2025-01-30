T,S = input().split()
total = 0

match T:
    case "のぞみ":
        total += 10000
    case "ひかり":
        total += 9000
    case "こだま":
        total += 8000
match S:
    case "指定席":
        total *= 1
    case "自由席":
        total -= 500
    case "グリーン車":
        total += 5000
print(total)
