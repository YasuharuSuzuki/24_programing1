C=list(input().split())
num_list=[]
for i in C:
    if i[1]=="J":
        num_list.append(11)
    elif i[1]=="Q":
        num_list.append(12)
    elif i[1]=="K":
        num_list.append(13)
    elif i[1]=="A":
        num_list.append(1)
    else:
        num_list.append(int(i[1:]))
num_list.sort()
dif_set={num_list[i+1]-num_list[i] for i in range(len(num_list)-1)}
if len(dif_set)==1:
    print("YES")
else:
    print("NO")