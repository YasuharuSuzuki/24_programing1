flowers = {'赤','白','黃','紫','桃'}
growing_flowers = set(input().split())
if len(growing_flowers) == 1:
    print(f'全部{growing_flowers.pop()}！')
elif len(growing_flowers) == 5:
    print('キレイだなぁ〜')
elif len(growing_flowers) == 4:
    print('{}が欲しいなぁ'.format(list(flowers - growing_flowers)[0]))
elif len(growing_flowers) == 2:
    print('{}と{}と{}が欲しいなぁ'.format(list(flowers - growing_flowers)[0],list(flowers - growing_flowers)[1],list(flowers - growing_flowers)[2]))
else:
    print('{}と{}が欲しいなぁ'.format(list(flowers - growing_flowers)[0],list(flowers - growing_flowers)[1]))
