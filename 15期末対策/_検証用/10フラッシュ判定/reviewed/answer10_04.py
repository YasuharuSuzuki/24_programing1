C_list = list(map(str, input().split()))
C_set = set()
for i in range(5):
    mozi = C_list[i]
    C_set.add(mozi[0])

if len(C_set) == 1:
    print("YES")
else:
    print("NO")
