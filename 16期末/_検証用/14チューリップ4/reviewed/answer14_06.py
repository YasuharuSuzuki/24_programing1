all_color = {'赤', '白' ,'黄', '桃'}
colors = set(input().split())
if len(colors) == 1:
    print(f'全部{colors.pop()}！')
elif len(colors) == 4:
    print('キレイだなぁ〜')
elif len(colors) == 3:
    print('{}が欲しいなぁ～'.format(list(all_color - colors)[0]))
else:
    print('{0[0]}と{0[1]}が欲しいなぁ～'.format(list(all_color - colors)))