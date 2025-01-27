S = str(input())
L_count = S.count("L")
R_count = S.count("R")
L_count2 = L_count * -1
aiueo = L_count2 + R_count
if -3 <= aiueo <= 3 :
    print("GOAL")
else:
    print("YOU LOST")