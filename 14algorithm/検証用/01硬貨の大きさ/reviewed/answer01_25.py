A,B = map(int,input().split())

size = {1:20.0,5:22.0,10:23.5,50:21.0,100:22.6,500:26.5}

if size[A] > size[B]:
    print("A")
elif size[A] < size[B]:
    print("B")
elif size[A] == size[B]:
    print("同じ")