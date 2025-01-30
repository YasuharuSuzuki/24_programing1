all_color = {'赤','白','黄','桃','紫'}
Ci = set(input().split())
if len(Ci) == 1:
    print(f'全部{Ci.pop()}！')
elif len(Ci) == 5:
    print('キレイだなぁ〜')
elif len(Ci) == 4:
    print('{}が欲しいなぁ～'.format(list(all_color - Ci)[0]))
elif len(Ci) == 3:
    print('{0[0]}と{0[1]}が欲しいなぁ～'.format(list(all_color - Ci)))
else:
    print('{0[0]}と{0[1]}と{0[2]}が欲しいなぁ～'.format(list(all_color - Ci)))