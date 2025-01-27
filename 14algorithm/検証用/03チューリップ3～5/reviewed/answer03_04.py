all_color = {'赤', '白', '黄', '紫'}
N = int(input())
Ci = set(input().split())
if len(Ci) == 1:
    print(f'全部{Ci.pop}！')
elif len(Ci) == 4:
    print('キレイだなぁ〜')
elif len(Ci) == 3:
    print('{}が欲しいなぁ～'.format(list(all_color - Ci)[0]))
else:
    print('{0[0]}と{0[1]}が欲しいなぁ～'.format(list(all_color - Ci)))