T, S = map(str,input().split())
if T == "のぞみ":
   if S == "指定席":
       print(10000)
   elif S == "自由席":
       print(9500)
   else:
       print(15000)
elif T == "ひかり":
   if S == "指定席":
       print(9000)
   elif S == "自由席":
       print(8500)
   else:
       print(14000)
elif T == "こだま":
   if S == "指定席":
       print(8000)
   elif S == "自由席":
       print(7500)
   else:
       print(13000)