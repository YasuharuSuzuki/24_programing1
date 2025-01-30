D = int(input())
K = str(input())
A = str(input())
Rcount = K.count("R")
Lcount = K.count("L")
Rcount2 = A.count("R")
Lcount2 = A.count("L")
M = (Lcount + Lcount2) * -1
A = Rcount + Rcount2 + K
if A > 3 or A < -3:
    print("YOU LOST")
else:
    print("GOAL")
