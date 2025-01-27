N = int(input())
all_color = {'赤','白','黃', '紫'}
input_set1 = set(input().split())
if len(input_set1) == 1:
    print(f'全部{input_set1.pop()}！')

elif len(input_set1) == 4:
    print('キレイだなぁ〜')
elif len(input_set1) == 3:
    nai = list(all_color - input_set1)
    print(f'{nai[0]}が欲しいなぁ')
elif len(input_set1) == 2:
    nai = list(all_color - input_set1)
    print(f'{nai[0]}と{nai[1]}が欲しいなぁ')