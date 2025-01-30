T,S=input().split()
match T:
  case "のぞみ":
      price=10000
  case "ひかり":
      price=9000
  case "こだま":
      price=8000
match S:
    case "自由席":
        price-=500
    case "グリーン車":
        price+=5000
print(price)