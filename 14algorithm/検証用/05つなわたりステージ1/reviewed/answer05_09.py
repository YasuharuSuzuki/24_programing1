katamuki = 0
time_count = 0
S = input()
for i in range(20):
  if S[i] == "L":
    katamuki += 1
    if katamuki >= 3:
        print("YOU LOST")
      break
    time_count += 1
  elif S[i] == "R":
    katamuki -= 1
    if katamuki <= -3:
        print("YOU LOST")
      break
    time_count += 1
  elif S[i] == "N":
    time_count += 1
if time_count == 20:
    print("GOAL")


