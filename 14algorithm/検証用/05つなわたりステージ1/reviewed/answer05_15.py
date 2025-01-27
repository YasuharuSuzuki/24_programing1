S = str(input())
Rcount = S.count("R")
Lcount = S.count("L")
K = Lcount * -1
A = Rcount + K
if A > 3 or A < -3:
    print("YOU LOST")
else:
    print("GOAL")