q16_f,q16_l=map(int,input().split())

days=0
for q16 in range(q16_f,q16_l+1):
    if q16%4==0:
        if q16%100==0:
            if q16%400==0:
                days=days+366
            else:
                days=days+365
        else:
            days=days+366
    else:
        days=days+365

print(days)
