def solve():
  s = input()
  left_tilt = 0
  right_tilt = 0

  for char in s:
    if char == 'L':
      left_tilt += 1
      right_tilt = max(0, right_tilt - 1)
    elif char == 'R':
      right_tilt += 1
      left_tilt = max(0, left_tilt - 1)

    if left_tilt > 3 or right_tilt > 3:
      print("YOU LOST")
      return

  print("GOAL")

solve()

