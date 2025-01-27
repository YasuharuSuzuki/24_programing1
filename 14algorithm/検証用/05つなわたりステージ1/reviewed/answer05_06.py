def solve():
  s = input()
  left_tilt = 0
  right_tilt = 0

  for move in s:
    if move == 'L':
      left_tilt += 1
      right_tilt = max(0, right_tilt - 1)
    elif move == 'R':
      right_tilt += 1
      left_tilt = max(0, left_tilt - 1)

    if left_tilt > 3 or right_tilt > 3:
      print("YOU LOST")
      return

  print("GOAL")

solve()

