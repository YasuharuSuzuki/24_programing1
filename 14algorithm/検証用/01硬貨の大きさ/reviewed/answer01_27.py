def solve():
  a, b = map(int, input().split())
  diameters = {
      1: 20.0,
      5: 22.0,
      10: 23.5,
      50: 21.0,
      100: 22.6,
      500: 26.5
  }

  diameter_a = diameters[a]
  diameter_b = diameters[b]

  if diameter_a > diameter_b:
    print("A")
  elif diameter_a < diameter_b:
    print("B")
  else:
    print("同じ")

solve()