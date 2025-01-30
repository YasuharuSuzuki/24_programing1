all_color = {'赤','白','黄','桃','紫'}
N = 5
C = input().split()

if len(set(C)) == 1:
    print(f"全部{C[0]}！")
elif len(set(C)) == 5:
    print("キレイだなぁ〜")
else:
    lost_colors = list(all_color - set(C))
    if len(lost_colors) == 1:
        print(f"{lost_colors[0]}が欲しいなぁ〜")
    elif len(lost_colors) == 2:
        print(f"{lost_colors[1]}と{lost_colors[0]}が欲しいなぁ〜")
    elif len(lost_colors) == 3:
        print(f"{lost_colors[1]}と{lost_colors[2]}と{lost_colors[0]}が欲しいなぁ〜")