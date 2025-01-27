all_color = ['赤','白','黃','紫']
kazu = int(input())
iro = set(input().split())

if len(iro) == 1:
    print(f'全部{iro}！')
elif len(iro) == 4:
    print('キレイだなぁ〜')
else:
    t = set(all_color) - iro
    a = list(t)
    if len(a) == 1:
        print(f'{a[0]}が欲しいなぁ')
    elif len(a) == 2:
        print(f'{a[0]}と{a[1]}が欲しいなぁ')

