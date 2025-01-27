S=list(input())
lean=0
ans=0
for i in S:
    if abs(lean)>3:
        ans="YOU LOST"
        print(ans)
        break
    elif i=="L":
        lean+=1
    elif i=="R":
        lean-=1
if ans!="YOU LOST":
    ans="GOAL"
    print(ans)