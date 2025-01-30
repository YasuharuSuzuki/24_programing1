all_color = {'赤','白','黄','桃','紫'}
input_set1 = set(input().split())
if len(input_set1) == 1:
    print(f'全部{input_set1.pop()}！')
elif len(input_set1) == 5:
    print('キレイだなぁ〜')
else:
    print('{}が欲しいなぁ'.format("と".join(list(all_color - input_set1))))
