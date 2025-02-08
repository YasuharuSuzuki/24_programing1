Y_s, Y_e = map(int,input().split())
days = 0
for y in range(Y_s,Y_e+1):
    days_per_year = 365
    if y%400 == 0:
        days_per_year = 366
    elif y%100 == 0:
        days_per_year = 365
    elif y%4 == 0:
        days_per_year = 366
    days += days_per_year

print(days)