all_color = {'赤','白','黃','紫'}
N = int(input())
C = input().split()

if len(set(C)) == 1:
    print(f"全部{C[0]}！")
elif len(set(C)) == 4:
    print("キレイだなぁ〜")
else:
    lost_colors = list(all_color - set(C))
    if len(lost_colors) == 1:
        print(f"{lost_colors[0]}が欲しいなぁ〜")
    elif len(lost_colors) == 2:
        print(f"{lost_colors[1]}と{lost_colors[0]}が欲しいなぁ〜")
