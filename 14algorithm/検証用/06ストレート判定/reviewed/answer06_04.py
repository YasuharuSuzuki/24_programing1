cards = input().split()
No = []

for card in cards:
  if card[-1] == 'A':
    No.append(1)
  elif card[-1] == 'J':
    No.append(11)
  elif card[-1] == 'Q':
    No.append(12)
  elif card[-1] == 'K':
    No.append(13)
  else:
    No.append(int(card[1:]))

No.sort()

straight = True

for i in range(4):
  if No[i+1] - No[i] != 1:
    straight = False
    break

if straight == True:
  print("YES")
else:
  print("NO")
