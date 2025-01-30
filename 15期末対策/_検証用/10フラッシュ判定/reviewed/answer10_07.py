cards_1=input().split()
cards_2=[]

for card in cards_1:
    suto=card[0]
    cards_2.append(str(suto))

#print(cards_2)

flash=False
for c in range(4):
    if cards_2[c]==cards_2[c+1]:
        flash=True
        break

if flash:
    print("YES")
else:
    print("NO")
