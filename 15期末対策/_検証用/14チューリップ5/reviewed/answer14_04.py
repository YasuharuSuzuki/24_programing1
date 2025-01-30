all_color = {'赤','白','黃','桃','紫'}
input_set1 = set(input().split())
nai = list(all_color - input_set1)

if len(input_set1) == 1:
    print(f'全部{input_set1.pop()}！')
elif len(input_set1) == 5:
    print('キレイだなぁ〜')
elif len(input_set1) == 4:
    print(f'{nai[0]}が欲しいなぁ')
elif len(input_set1) == 3:
    print(f'{nai[0]}と{nai[1]}が欲しいなぁ')
elif len(input_set1) == 2:
    print(f'{nai[0]}と{nai[1]}と{nai[2]}が欲しいなぁ')

