flowers = {'赤','白','黃','紫'}
N, = map(int,input().split())
growing_flowers = set(input().split())
if len(growing_flowers) == 1:
    print(f'全部{growing_flowers.pop()}！')
elif len(growing_flowers) == 4:
    print('キレイだなぁ〜')
elif len(growing_flowers) == 3:
    print('{}が欲しいなぁ'.format(list(flowers - growing_flowers)[0]))
else:
    print('{}と{}が欲しいなぁ'.format(list(flowers - growing_flowers)[0],list(flowers - growing_flowers)[1]))


