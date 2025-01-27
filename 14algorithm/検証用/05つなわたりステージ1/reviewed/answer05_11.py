sousa=input()

iti=0

for sayuu in sousa:
    if sayuu == 'L':
        iti += 1
    elif sayuu == 'R':
        iti -= 1
    if abs(iti) > 3:
        print("YOU LOST")
        break
else:
    print("GOAL")