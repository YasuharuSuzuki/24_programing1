all_color = {'赤','白','黄','桃' }
yururu_set = set(input().split())
if len(yururu_set) == 1:
    print(f'全部{yururu_set.pop()}！')
elif len(yururu_set) == 4:
    print('キレイだなぁ〜')
else:
    print(f'{"と".join(list(all_color - yururu_set))}が欲しいなぁ〜')