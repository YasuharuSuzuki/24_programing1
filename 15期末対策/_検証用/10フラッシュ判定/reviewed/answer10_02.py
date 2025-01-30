C_list=input().split()
C_set=set()
for i in C_list:
    C_set.add(i[0])
if len(C_set)==1:
    print("YES")
else:
    print("NO")