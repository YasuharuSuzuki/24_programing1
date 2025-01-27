A,B = map(int,input().split())

match A:
  case 1: A_size = 20.0
  case 5: A_size = 22.0
  case 10:A_size  = 23.5
  case 50:A_size = 21.0
  case 100:A_size = 22.6
  case 500:A_size = 26.5
print(A_size)

match B:
  case 1: B_size = 20.0
  case 5: B_size = 22.0
  case 10:B_size  = 23.5
  case 50:B_size = 21.0
  case 100:B_size = 22.6
  case 500:B_size = 26.5
print(B_size)

if A > B:
  print(A)
elif A < B:
  print(B)
else:
  print("同じ")

