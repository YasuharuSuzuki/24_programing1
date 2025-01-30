colors = input().split()
if len(set(colors)) == 1:
      print(f"全部{colors[0]}！")

elif set(colors) == set(["赤", "白", "黄", "桃", "紫"]):
    print("キレイだなぁ〜")

else:
    all_colors = ["赤", "白", "黄", "桃", "紫"]
    want_colors = [color for color in all_colors if color not in colors]

    if len(want_colors) == 1:
        print(f"{want_colors[0]}が欲しいなぁ〜")
    elif len(want_colors) == 2:
        print(f"{want_colors[0]}と{want_colors[1]}が欲しいなぁ〜")
    elif len(want_colors) == 3:
        print(f"{want_colors[0]}と{want_colors[1]}と{want_colors[2]}が欲しいなぁ〜")