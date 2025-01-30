t,s = map(str, input().split())
n = 0
r = 0
if t == "こだま":
    n = 8000
if t == "ひかり":
    n = 9000
if t == "のぞみ":
    n = 10000
if s == "指定席":
    r = n
if s =="自由席":
    r = n-500
if s =="グリーン車":
    r = n+5000
print(r)