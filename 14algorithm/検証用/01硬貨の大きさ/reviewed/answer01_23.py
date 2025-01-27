a, b = map(int, input(). split())
kouka = [1, 50, 100, 10, 500]
A = kouka.index(a)
B = kouka.index(b)
if A < B:
    print("B")
elif A > B:
    print("A")
else:
    print("同じ")