D=int(input())
K=input().split()
A=input().split()
#K=input()
#A=input()
data=0
for i,j in zip(K,A):
    if i=="L":
        data+=1
    elif i=="R":
        data-=1
    if j=="L":
        data+=1
    elif j=="R":
        data-=1
    if abs(data)>3:
        print("YOU LOST")
        break
else:
    print("GOAL")