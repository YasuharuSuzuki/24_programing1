cards_1=input().split()
cards_2=[]

for card in cards_1:
    number=card[1:]
    if number=="A":
        cards_2.append(1)
    elif number=="J":
        cards_2.append(11)
    elif number=="Q":
        cards_2.append(12)
    elif number=="K":
        cards_2.append(13)
    else:
        cards_2.append(int(number))

cards_2.sort()
sutoreeto=True
for c in range(4):
    if cards_2[c]+1!=cards_2[c+1]:
        sutoreeto=False
        break

if sutoreeto:
    print("YES")
else:
    print("NO")