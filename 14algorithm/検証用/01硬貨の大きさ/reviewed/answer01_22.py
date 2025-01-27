A,B = map(int,input().split())

en = {1:20.0,5:22.0,10:23.5,50:21.0,100:22.6,500:26.5}

if en[A] > en[B]:
  print("A")
elif en[A] < en[B]:
  print("B")
elif en[A] == en[B]:
  print("同じ")

