all_color = {'赤','白','黄','紫'}
N = int(input())
purchased_color = input().split()
colors = set(purchased_color)
if len(colors) == 1:
    print(f"全部{purchased_color[0]}！")
elif colors == all_color:
    print('キレイだなぁ〜')
else:
    no_color = all_color - colors
    print(f"{'と'.join(no_color)}が欲しいなぁ～")