S = input()
idou_list = list(map(int,S.split()))
L = idou_list.count('L')
R = idou_list.count('R')
yururu = 20+1*L-1*R
if yururu >= 0:
  print("GOAL")
else:
  print("YOU LOST")

