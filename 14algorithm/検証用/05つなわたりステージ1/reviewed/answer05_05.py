s = input()

L = 0
R = 0

for yururu in s:
  if yururu == "L":
    L += 1
    R -= 1
  elif yururu == "R":
    R += 1
    L -= 1
  if L > 3 or R > 3:
    print("YOU LOST")
    break
else:
  print("GOAL")