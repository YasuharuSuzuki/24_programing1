D = int(input())
K = str(input())
A = str(input())
yururu = 0
L_count = K.count("L")
yururu += L_count
R_count = K.count("R")
yururu -= R_count

L_count2 = A.count("L")
yururu += L_count2
R_count2 = A.count("R")
yururu -= R_count2

if -3 <= yururu and yururu <= 3 :
    print("GOAL")
else:
    print("YOU LOST")
