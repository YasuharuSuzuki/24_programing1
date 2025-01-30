a,b = map(str,input().split())

if a == "のぞみ":
    kingaku = 10000
elif a == "ひかり":
    kingaku = 9000
else:
    kingaku = 8000

if b == "自由席":
    kingaku -= 500
elif b == "グリーン車" :
    kingaku += 5000
print(kingaku)