all_color = {'赤','白','黃','紫'}
set1 = set(input().split())
if len(set1) == 1:
    print(f'全部{set1.pop()}！')
elif len(set1) == 4:
    print('キレイだなぁ〜')
elif len(set1) == 3:
    print('{}が欲しいなぁ～'.format(list(all_color - set1)[0]))
else:
    print('{}と{}が欲しいなぁ～'.format(list(all_color - set1)[0] , list(all_color - set1)[1]))

