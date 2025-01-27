all_color = {'赤','白','黄','紫'}
flower_num = int(input())
input_set1 = set(input().split())
if len(input_set1) == 1:
    print(f'全部{input_set1.pop()}！')
elif all_color & input_set1 == all_color:
    print('キレイだなぁ～')
else:
    color_n = all_color - input_set1
    if len(color_n) == 1:
        print(f'{color_n.pop()}が欲しいなぁ～')
    elif len(color_n) == 2:
        color_n = list(color_n)
        print(f'{color_n[0]}と{color_n[1]}が欲しいなぁ～')
