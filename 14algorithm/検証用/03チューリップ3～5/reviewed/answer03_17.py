all_color = {'赤','白','黄','紫'}
a = int(input())
input_set1 = set(input().split())
if len(input_set1) == 1:
    print(f'全部{input_set1.pop()}！')
elif len(input_set1) == 4:
    print('キレイだなぁ〜')
else:
    t = list(all_color - input_set1)
    if len(t) == 1:
        print(f'{t[0]}が欲しいなぁ')
    else:
        print(f'{t[0]}と{t[1]}が欲しいなぁ')

