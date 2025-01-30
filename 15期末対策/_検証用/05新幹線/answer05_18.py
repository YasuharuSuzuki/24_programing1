T,S=input().split()
print(T,S)
if T=="のぞみ":
  kihonn=10000
elif T=="ひかり":
    kihonn=9000
elif T=="こだま":
      kihonn=8000
else :
      print("間違っています")
if S=="指定席":
  print(kihonn)
elif S=="自由席":
  print(kihonn-500)
elif S=="グリーン車":
    print(kihonn+5000)
else :
      print("間違っています")
