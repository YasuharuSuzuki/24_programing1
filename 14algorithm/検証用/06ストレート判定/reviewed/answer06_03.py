C_list = list(map(str, input().split()))
D_list = []
seikai = 0
for i in range(5):
    suzi = C_list[i]
    if len(suzi) == 3:
        suzi = 10
    else:
        suzi = suzi[1]
    if suzi == "J" :
        suzi = 11
    elif suzi == "Q" :
        suzi = 12
    elif suzi == "K" :
        suzi = 13
    elif suzi == "A" :
        suzi = 1
    suzi = int(suzi)
    D_list.append(suzi)

    #print(f"数字{suzi}")

D_list.sort()


for count in range(4):
    if D_list[count] + 1 == D_list[count + 1]:
        seikai += 1
    #print(f"今のカウント = {D_list[count]}")
    #print(f"次のカウント = {D_list[count]+1}")
    #print(f"今のカウント+1={D_list[count+1]}")
    #print(seikai)

if seikai == 4:
    print("YES")
else:
    print("NO")

