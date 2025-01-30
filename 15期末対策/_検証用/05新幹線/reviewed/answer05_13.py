T,S=input().split()

match T:
    case "のぞみ":
        if S=="指定席":
            print(10000)
        elif S=="自由席":
            print(10000-500)
        else:
            print(10000+5000)
    case "ひかり":
        if S=="指定席":
            print(9000)
        elif S=="自由席":
            print(9000-500)
        else:
            print(9000+5000)
    case "こだま":
        if S=="指定席":
            print(8000)
        elif S=="自由席":
            print(8000-500)
        else:
            print(8000+5000)