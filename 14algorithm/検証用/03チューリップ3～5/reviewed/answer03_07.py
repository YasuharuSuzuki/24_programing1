def solve():
    n = int(input())
    colors = input().split()

    unique_colors = set(colors)

    if len(unique_colors) == 1:
        print(f"全部{colors[0]}！")
    elif len(unique_colors) == 4:
        print("キレイだなぁ〜")
    else:
        all_colors = {"赤", "白", "黄", "紫"}
        missing_colors = list(all_colors - unique_colors)

        if len(missing_colors) == 1:
            print(f"{missing_colors[0]}が欲しいなぁ〜")
        else:
            print(f"{missing_colors[0]}と{missing_colors[1]}が欲しいなぁ〜")

solve()