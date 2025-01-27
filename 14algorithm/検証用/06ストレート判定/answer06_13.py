def card_to_value(card):
  if card[-1].isdigit():
    return int(card[-1]) if len(card)==2 else int(card[-2:])
  elif card[-1] == 'J':
    return 11
  elif card[-1] == 'Q':
    return 12
  elif card[-1] == 'K':
    return 13
  elif card[-1] == 'A':
    return 1
  else:
    return 0


def is_straight(cards):
  values = [card_to_value(card) for card in cards]
  values.sort()

  for i in range(len(values) - 1):
    if values[i + 1] - values[i] != 1:
      if values[0] == 1 and values[-1] == 13 and values[1] == 2 and values[2] == 3 and values[3] == 4:
        return True
      else:
        return False
  return True

cards = input().split()

if is_straight(cards):
  print("YES")
else:
  print("NO")


