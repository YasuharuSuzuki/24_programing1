C = list(input().split())
suto = set()
for i in C:
    suto.add(i[0])
if len(suto) == 1:
    print("YES")
else:
    print("NO")