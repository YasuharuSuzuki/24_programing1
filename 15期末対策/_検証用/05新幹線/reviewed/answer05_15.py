T,S = input().split()
if T == 'のぞみ':
  A = (10000)
elif T == 'ひかり':
  A = (9000)
elif T == 'こだま':
  A = (8000)
if S == '指定席':
  B = (0)
elif S == '自由席':
  B = (-500)
elif S == 'グリーン車':
  B = (5000)
print(A + B)
