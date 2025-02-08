Ys,Ye=map(int,input().split())
data=0
for year in range(Ys,Ye+1):
    if year%4==0 and (year%100!=0 or year%400==0):
        data+=366
    else:
        data+=365
print(data)