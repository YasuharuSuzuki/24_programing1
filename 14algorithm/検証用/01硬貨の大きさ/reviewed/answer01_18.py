a,b = map(int,input().split())
kouka = [1, 50, 5, 100, 10, 500]
a1 = kouka.index(a)
b1 = kouka.index(b)

if a1 > b1:
    print("A")
elif b1 > a1:
    print("B")
else:
    print("同じ")
