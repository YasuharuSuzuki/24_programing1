all_color = {'赤','白','黃','紫'}
N = int(input())
Cn = set(input().split())
if len(Cn) == 1:
    print(f'全部{Cn.pop()}！')
elif len(Cn) == 4:
    print('キレイだなぁ〜')
elif len(Cn) == 2:
    diff_list = list(all_color - Cn)
    print('{}と{}が欲しいなぁ'.format(list(diff_list)[0],(diff_list)[1]))
else:
    print('{}が欲しいなぁ'.format(list(all_color - Cn)[0]))
