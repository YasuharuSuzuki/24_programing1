N = int(input())
C = list(input().split())
all_color = ["赤","白","黄"]

if len(C) == N:
    if len(set(C)) == 1:
        print(f"全部{C[0]}!")
    elif len(set(C)) == 4:
        print("キレイだな～")
    else:
        C = list(set(all_color) - set(C))
        if len(C) == 1:
            print(f"{C[0]}が欲しいなぁ～")
        elif len(C) == 2:
            print(f"{C[0]}と" + f"{C[1]}が欲しいなぁ～")

