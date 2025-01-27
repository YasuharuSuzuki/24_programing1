kouka = [1, 5, 10, 50, 100, 500]
nagasa = [20.0, 22.0, 23.5, 21.0, 22.6, 26.5]
An, Bn = map(int,input().split())

for i, e in enumerate(kouka):
    if An == e:
        A1 = i
        break
i = 0
for i, e in enumerate(kouka):
    if Bn == e:
        B1 = i
        break

if A1 == B1:
    print("同じ")
elif nagasa[A1] > nagasa[B1]:
    print("A")
else:
    print("B")