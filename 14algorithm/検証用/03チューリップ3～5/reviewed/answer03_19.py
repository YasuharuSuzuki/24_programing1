n = int(input())
colors = input().split()

unique_colors = set(colors)

if len(unique_colors) == 1:
  print(f"全部{colors[0]}！")
elif unique_colors == {"赤", "白", "黄", "紫"}:
  print("キレイだなぁ〜")
else:
    missing_colors = []
    all_colors = ["赤", "白", "黄", "紫"]
    for color in all_colors:
        if color not in unique_colors:
          missing_colors.append(color)

    if len(missing_colors) == 1:
        print(f"{missing_colors[0]}が欲しいなぁ〜")
    elif len(missing_colors) == 2:
        print(f"{missing_colors[0]}と{missing_colors[1]}が欲しいなぁ〜")

