al_color = {"赤","白","黄","桃"}
C = set(input().split())
nocolor = (al_color - C)

if len(nocolor) == 3:
    print(f"全部{list(C)[0]}!")
elif len(nocolor) == 2:
    print(f"{list(nocolor)[0]}と{list(nocolor)[1]}が欲しいなぁ〜")
elif len(nocolor) == 1:
    print(f"{list(nocolor)[0]}が欲しいなぁ〜")
else:
    print(f"キレイだなぁ〜")